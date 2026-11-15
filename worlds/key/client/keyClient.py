import asyncio
from CommonClient import CommonContext, get_base_parser, gui_enabled, server_loop
from worlds.LauncherComponents import launch


class KirbyYarnContext(CommonContext):
    # Text Mode to use !hint and such with games that have no text entry
    game = "Kirby's Epic Yarn"  # empty matches any game since 0.3.2
    items_handling = 0b111  # receive all items for /received

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
        """
        Initialize the GUI for The Wind Waker client.

        :return: The client's GUI.
        """
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