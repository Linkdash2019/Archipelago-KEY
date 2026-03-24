import asyncio
import traceback
from typing import TYPE_CHECKING, Any, Optional

from . import background
from . import setupSaveFile
import dolphin_memory_engine as dme

import Utils
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, logger, server_loop

if TYPE_CHECKING:
    import kvui

SAVED_ITEMS = []

CONNECTION_REFUSED_GAME_STATUS = (
    "Dolphin failed to connect. Please load a ROM for Kirby's Epic Yarn. Trying again in 5 seconds..."
)
CONNECTION_REFUSED_SAVE_STATUS = (
    "Dolphin failed to connect. Please load into save file 1. Trying again in 5 seconds..."
)
CONNECTION_LOST_STATUS = (
    "Dolphin connection was lost. Please restart your emulator and make sure Kirby's Epic Yarn is running."
)
CONNECTION_CONNECTED_STATUS = "Dolphin connected successfully."
CONNECTION_INITIAL_STATUS = "Dolphin connection has not been initiated."


class KEYCommandProcessor(ClientCommandProcessor):
    """
    Command Processor for Kirby Epic Yarn client commands.

    This class handles commands specific to Kirby Epic Yarn.
    """

    def __init__(self, ctx: CommonContext):
        """
        Initialize the command processor with the provided context.

        :param ctx: Context for the client.
        """
        super().__init__(ctx)

    def _cmd_dolphin(self) -> None:
        """
        Display the current Dolphin emulator connection status.
        """
        if isinstance(self.ctx, KEYContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")


class KEYContext(CommonContext):
    """
    The context for Kirby Epic Yarn client.

    This class manages all interactions with the Dolphin emulator and the Archipelago server for Kirby's Epic Yarn.
    """

    command_processor = KEYCommandProcessor
    game: str = "Kirby's Epic Yarn"
    items_handling: int = 0b111

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        """
        Initialize the KEY context.

        :param server_address: Address of the Archipelago server.
        :param password: Password for server authentication.
        """

        super().__init__(server_address, password)
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.dolphin_status: str = CONNECTION_INITIAL_STATUS
    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        """
        Disconnect the client from the server and reset game state variables.

        :param allow_autoreconnect: Allow the client to auto-reconnect to the server. Defaults to `False`.

        """
        self.auth = None

        await super().disconnect(allow_autoreconnect)

    async def server_auth(self, password_requested: bool = False) -> None:
        """
        Authenticate with the Archipelago server.

        :param password_requested: Whether the server requires a password. Defaults to `False`.
        """
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        if not self.auth:
            logger.info("Enter you slot name:")
            self.auth = await self.console_input()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict[str, Any]) -> None:
        """
        Handle incoming packages from the server.

        :param cmd: The command received from the server.
        :param args: The command arguments.
        """
        if cmd == "Connected":
            pass
        elif cmd == "Retrieved":
            requested_keys_dict = args["keys"]

    def make_gui(self) -> type["kvui.GameManager"]:
        """
        Initialize the GUI for Kirby's Epic Yarn client.

        :return: The client's GUI.
        """
        ui = super().make_gui()
        ui.base_title = "Archipelago Kirby's Epic Yarn Client"
        return ui

async def dolphin_sync_task(ctx: KEYContext) -> None:
    """
    The task loop for managing the connection to Dolphin.

    While connected, read the emulator's memory to look for any relevant changes made by the player in the game.

    :param ctx: Kirby's Epic Yarn client context.
    """
    logger.info("Starting Dolphin connector. Use /dolphin for status information.")
    sleep_time = 0.0
    while not ctx.exit_event.is_set():
        if sleep_time > 0.0:
            try:
                # ctx.watcher_event gets set when receiving ReceivedItems or LocationInfo, or when shutting down.
                await asyncio.wait_for(ctx.watcher_event.wait(), sleep_time)
            except asyncio.TimeoutError:
                pass
            sleep_time = 0.0
        ctx.watcher_event.clear()

        try:
            if dme.is_hooked() and ctx.dolphin_status == CONNECTION_CONNECTED_STATUS:
                try:
                    if dme.read_byte(0x906A6C4F) in range(0x01, 0xFE):
                        # Check if still save file 1
                        logger.info(CONNECTION_REFUSED_SAVE_STATUS)
                        ctx.dolphin_status = CONNECTION_REFUSED_SAVE_STATUS
                        dme.un_hook()
                        sleep_time = 5
                        continue
                except:
                    # Check if still connected
                    logger.info("Connection to Dolphin lost, reconnecting...")
                    ctx.dolphin_status = CONNECTION_LOST_STATUS
                    dme.un_hook()
                    continue
                if ctx.slot is not None:
                    # Do stuff, (Check locations, Give Rewards, Etc. dme)
                    print(ctx.items_received)
                    for item in ctx.items_received:
                        logger.info(item)
                        if item not in SAVED_ITEMS:
                            SAVED_ITEMS.append(item)
                setupSaveFile.setup()
                background.redirectBossDoors()
                background.motifFix()
                sleep_time = 0.1
            else:
                logger.info("Attempting to connect to Dolphin...")
                dme.hook()
                if dme.is_hooked():
                    # Check if game is Kirby Epic Yarn
                    if dme.read_bytes(0x80000000, 6) != b"RK5E01":
                        logger.info(CONNECTION_REFUSED_GAME_STATUS)
                        ctx.dolphin_status = CONNECTION_REFUSED_GAME_STATUS
                        dme.un_hook()
                        sleep_time = 5
                    # Check if save file 1 is loaded
                    elif dme.read_byte(0x906A6C4F) in range(0x01, 0xFE):
                        logger.info(CONNECTION_REFUSED_SAVE_STATUS)
                        ctx.dolphin_status = CONNECTION_REFUSED_SAVE_STATUS
                        dme.un_hook()
                        sleep_time = 5
                    # If connected to Dolphin
                    else:
                        logger.info(CONNECTION_CONNECTED_STATUS)
                        ctx.dolphin_status = CONNECTION_CONNECTED_STATUS
                        ctx.locations_checked = set()
                else:
                    logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
                    ctx.dolphin_status = CONNECTION_LOST_STATUS
                    await ctx.disconnect()
                    sleep_time = 5
                    continue
        except Exception:
            dme.un_hook()
            logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
            logger.error(traceback.format_exc())
            ctx.dolphin_status = CONNECTION_LOST_STATUS
            await ctx.disconnect()
            sleep_time = 5
            continue


def main(*args: str) -> None:
    """
    Run the main async loop for the Kirby Epic Yarn client.

    :param *args: Command line arguments passed to the client.
    """
    Utils.init_logging("Kirby's Epic Yarn Client")

    async def _main(connect: Optional[str], password: Optional[str]) -> None:
        ctx = KEYContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await asyncio.sleep(1)

        ctx.dolphin_sync_task = asyncio.create_task(dolphin_sync_task(ctx), name="DolphinSync")

        await ctx.exit_event.wait()
        # Wake the sync task, if it is currently sleeping, so it can start shutting down when it sees that the
        # exit_event is set.
        ctx.watcher_event.set()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.dolphin_sync_task:
            await ctx.dolphin_sync_task

    parser = get_base_parser()
    parsed_args = parser.parse_args(args)

    import colorama

    colorama.init()
    asyncio.run(_main(parsed_args.connect, parsed_args.password))
    colorama.deinit()
