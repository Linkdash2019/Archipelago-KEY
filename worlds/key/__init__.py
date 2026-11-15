from .world import KirbyYarnWorld as KirbyYarnWorld
from worlds.LauncherComponents import Component, Type, components, icon_paths, launch

def startClient():
    from .client.keyClient import client
    launch(client, name="Kirby's Epic Yarn")


components.append(
    Component(
        "Kirby's Epic Yarn",
        component_type=Type.CLIENT,
        func=startClient,
        game_name="Kirby's Epic Yarn",
        supports_uri=False,
        #description="Launch the Kirby Epic Yarn Client."
    )
)
