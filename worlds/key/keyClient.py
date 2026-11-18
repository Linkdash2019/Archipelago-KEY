import asyncio
import dolphin_memory_engine as dme
from CommonClient import CommonContext, get_base_parser, gui_enabled, server_loop, ClientCommandProcessor, logger
from Utils import async_start
from worlds.LauncherComponents import launch

from .locations import LOCATION_NAME_TO_ID
from .items import allItems

class KirbyYarnCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_dolphin(self) -> None:
        """
        Helpful hint on how this command works
        """
        print("Dolphin Command Test!")
        itemsReceivedStr = []
        for item in self.ctx.items_received:
            itemDict = item._asdict()
            itemName = allItems[itemDict["item"]-2]
            itemsReceivedStr.append(itemName)
        self.output(str(itemsReceivedStr))

    def _cmd_check(self, check: str="") -> bool:
        """
        Simulate checking game location
        """
        if check:
            self.output("Checking game location " + check)
            checkID = LOCATION_NAME_TO_ID[check]
            if checkID is None:
                self.output("Game location " + check + " not found.")
                return False
            async_start( self.ctx.send_msgs([{"cmd": "LocationChecks", "locations": [checkID]}]))
            return True
        else:
            self.output("Please specify a location to be checked")
            self.output("(Example: /check 'Patch Castle Goal'")
            return False

class KirbyYarnContext(CommonContext):
    game = "Kirby's Epic Yarn"
    items_handling = 0b111  # receive all items for /received
    command_processor = KirbyYarnCommandProcessor

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(KirbyYarnContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game="Kirby's Epic Yarn")

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.game = "Kirby's Epic Yarn"
        await super().disconnect(allow_autoreconnect)

    def make_gui(self) -> type["kvui.GameManager"]:
        ui = super().make_gui()
        ui.base_title = "Kirby's Epic Yarn Client for Archipelago"
        return ui

async def dolphinLoop(ctx: KirbyYarnContext):
    while not ctx.exit_event.is_set():
        try:
            if dme.is_hooked():
            #If already connected
                if dme.read_bytes(0x80000000, 6) != b"RK5E01":
                    logger.info("Error lost connection. WRONG GAME!")
                    logger.info("Reconnecting to Dolphin in 5 seconds...")
                    dme.un_hook()
                    await asyncio.sleep(5)
                elif dme.read_byte(0x906A6C4F) in range(0x01, 0xFE):
                    logger.info("Error lost connection. Please load save file 1!")
                    logger.info("Reconnecting to Dolphin in 5 seconds...")
                    dme.un_hook()
                    await asyncio.sleep(5)
                else:
                    if (dme.read_byte(0x906A6C4F) == 0x00) and (ctx.slot is not None):
                        logger.info("Interacting with the game!")
                        itemsReceivedStr = []
                        for item in ctx.items_received:
                            itemDict = item._asdict()
                            itemName = allItems[itemDict["item"] - 2]
                            itemsReceivedStr.append(itemName)
                        logger.info(str(itemsReceivedStr))
                    await asyncio.sleep(2)
            else:
            #Setup connection
                logger.info("Attempting to connect to Dolphin...")
                dme.hook()
                if dme.is_hooked():
                    # Check if game is Kirby Epic Yarn
                    if dme.read_bytes(0x80000000, 6) != b"RK5E01":
                        logger.info("Error connecting. WRONG GAME!")
                        logger.info("Reconnecting to Dolphin in 5 seconds...")
                        dme.un_hook()
                        await asyncio.sleep(5)
                    # Check if save file 1 is loaded
                    elif dme.read_byte(0x906A6C4F) in range(0x01, 0xFE):
                        logger.info("Error connecting. Please load save file 1!")
                        logger.info("Reconnecting to Dolphin in 5 seconds...")
                        dme.un_hook()
                        await asyncio.sleep(5)
                    # If connected to Dolphin
                    else:
                        logger.info("Connected to Dolphin!")
                else:
                    logger.info("Connection to Dolphin failed. Trying again in 5 seconds...")
                    await asyncio.sleep(5)
        except Exception as error:
            dme.un_hook()
            logger.info("Generic Error:")
            logger.info(error)

async def main():
    ctx = KirbyYarnContext()
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()
    await asyncio.sleep(1)

    ctx.dolphinLoop = asyncio.create_task(dolphinLoop(ctx), name="DolphinLoop")

    await ctx.exit_event.wait()
    await ctx.shutdown()
    if ctx.dolphinLoop:
        await ctx.dolphinLoop

def client():
    import colorama

    parser = get_base_parser(description="Kirby's Epic Yarn Client")

    # use colorama to display colored text highlighting on windows
    colorama.just_fix_windows_console()

    asyncio.run(main())
    colorama.deinit()

if __name__ == "__main__":
    client()