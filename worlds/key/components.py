from worlds.LauncherComponents import SuffixIdentifier, Component, Type, components, launch

def run_client(*args: str) -> None:
    """
    Launch the Kirby Epic Yarn client.

    :param *args: Variable length argument list passed to the client.
    """
    print("Running the Kirby Epic Yarn Client")
    from .Client.KEYClient import main

    launch(main, name="KirbyEpicYarnClient", args=args)



components.append(
    Component(
        "Kirby's Epic Yarn",
        func=run_client,
        game_name="Kirby's Epic Yarn",
        component_type=Type.CLIENT,
        #file_identifier=SuffixIdentifier(".apkey"),
    )
)