import asyncio
from CommonClient import CommonContext, get_base_parser, gui_enabled, server_loop, ClientCommandProcessor
from Utils import async_start
from worlds.LauncherComponents import launch

from .locations import LOCATION_NAME_TO_ID

class KirbyYarnCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_dolphin(self) -> None:
        """
        Helpful hint on how this command works
        """
        print("Dolphin Command Test!")

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

async def main():
    ctx = KirbyYarnContext()
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    await ctx.exit_event.wait()
    await ctx.shutdown()

def client():
    import colorama

    parser = get_base_parser(description="Kirby's Epic Yarn Client")

    # use colorama to display colored text highlighting on windows
    colorama.just_fix_windows_console()

    asyncio.run(main())
    colorama.deinit()

if __name__ == "__main__":
    client()