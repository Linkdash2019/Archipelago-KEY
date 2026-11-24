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

    def _cmd_setup(self):
        """
        Setup file 1 for Archipelago use.
        For the best results file 1 MUST be empty
        """
        if self.ctx.isDolphinConnected:
            self.ctx.scheduleSetup = True
        else:
            self.output("Dolphin not connected.\nUnable to run setup.")

class KirbyYarnContext(CommonContext):
    game = "Kirby's Epic Yarn"
    items_handling = 0b111
    command_processor = KirbyYarnCommandProcessor

    isDolphinConnected = False
    scheduleSetup = False

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
    def un_hook_op():
        ### 'op' stands for 'operation'
        ctx.isDolphinConnected = False
        dme.un_hook()

    def file_setup_task():
        logger.info("Running setup.")
        # Unlock Badges
        hops = 0
        offset = 12
        while hops <= 40:
            level = 0x906A8F77 + (hops * offset)
            dme.write_byte(level, 0x03)
            hops += 1

        # Watch Cutscenes
        # (Also known as 'Flicks')
        ### Even though we unlock every cutscene
        ### the game will always play the cutscene if
        ### you entered the level with a door status of 0x02
        dme.write_byte(0x906A962B, 0x03)
        dme.write_byte(0x906A9637, 0x03)
        dme.write_byte(0x906A9643, 0x03)
        dme.write_byte(0x906A964F, 0x03)
        dme.write_byte(0x906A965B, 0x03)
        dme.write_byte(0x906A9667, 0x03)
        dme.write_byte(0x906A9673, 0x03)
        dme.write_byte(0x906A967F, 0x03)
        dme.write_byte(0x906A968B, 0x03)

        # Dialogs
        dme.write_byte(0x906A96F7, 0x03)
        dme.write_byte(0x906A973F, 0x03)
        dme.write_byte(0x906A971B, 0x03)
        dme.write_byte(0x906A96EB, 0x03)

        # Unlock Map (0x10) Unlock Magic Sock (0x14) Unlock shop doors (0xFF)
        dme.write_byte(0x906A7007, 0xFF)

        # Give apartment an owner
        # (To unlock only Kirby's pad do x00 x82)
        # (For everything to xFF xFF)
        # IMPORTANT: Does not open apartment doors
        dme.write_bytes(0x906A7005, b"\x00\x82")

        # Unlock shops
        dme.write_byte(0x906A7002, 0x01)  # Show merchants

        # Unlock all boss doors + patch castle
        dme.write_byte(0x906A7067 + (0 * 36), 0x03)
        dme.write_byte(0x906A7067 + (43 * 36), 0x03)
        dme.write_byte(0x906A7067 + (44 * 36), 0x03)
        dme.write_byte(0x906A7067 + (45 * 36), 0x03)
        dme.write_byte(0x906A7067 + (46 * 36), 0x03)
        dme.write_byte(0x906A7067 + (47 * 36), 0x03)
        dme.write_byte(0x906A7067 + (48 * 36), 0x03)

        # Don't run setup again this session
        ctx.scheduleSetup = False
        logger.info("Setup complete! You may now load file 1.")

    while not ctx.exit_event.is_set():
        try:
            #If connected to Dolphin
            if dme.is_hooked():
                #Check if game is Kirby Epic Yarn
                if dme.read_bytes(0x80000000, 6) != b"RK5E01":
                    logger.info("Error lost connection. WRONG GAME!")
                    logger.info("Reconnecting to Dolphin in 5 seconds...")
                    un_hook_op()
                    await asyncio.sleep(5)

                # Check if save file 1 or tile screen are loaded
                elif dme.read_byte(0x906A6C4F) in range(0x01, 0xFE):
                    logger.info("Error lost connection. Please load save file 1!")
                    logger.info("Reconnecting to Dolphin in 5 seconds...")
                    un_hook_op()
                    await asyncio.sleep(5)

                # If connected to Dolphin
                else:
                    # New game setup
                    if ctx.scheduleSetup:
                        if dme.read_byte(0x906A6C4F) == 0xFF:
                            file_setup_task()
                        else:
                            logger.info("Setup can not continue\nPlease return to the title screen.")
                            ctx.scheduleSetup = False

                    if (dme.read_byte(0x906A6C4F) == 0x00) and (ctx.slot is not None):
                        #Get received item names
                        itemsReceivedStr = []
                        for item in ctx.items_received:
                            itemDict = item._asdict()
                            itemName = allItems[itemDict["item"] - 2]
                            itemsReceivedStr.append(itemName)
                        logger.info(str(itemsReceivedStr))

                    await asyncio.sleep(2)

            #If dolphin not connected
            else:
                logger.info("Attempting to connect to Dolphin...")
                dme.hook()
                if dme.is_hooked():
                    # Check if game is Kirby Epic Yarn
                    if dme.read_bytes(0x80000000, 6) != b"RK5E01":
                        logger.info("Error connecting. WRONG GAME!")
                        logger.info("Reconnecting to Dolphin in 5 seconds...")
                        un_hook_op()
                        await asyncio.sleep(5)

                    # Check if save file 1 or tile screen are loaded
                    elif dme.read_byte(0x906A6C4F) in range(0x01, 0xFE):
                        logger.info("Error connecting. Please load save file 1!")
                        logger.info("Reconnecting to Dolphin in 5 seconds...")
                        un_hook_op()
                        await asyncio.sleep(5)

                    # If connected to Dolphin
                    else:
                        ctx.isDolphinConnected = True
                        logger.info("Connected to Dolphin!")
                else:
                    logger.info("Connection to Dolphin failed. Trying again in 5 seconds...")
                    await asyncio.sleep(5)

        except Exception as error:
            un_hook_op()
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