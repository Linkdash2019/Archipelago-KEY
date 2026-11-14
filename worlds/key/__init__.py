from .world import KirbyYarnWorld as KirbyYarnWorld
from worlds.LauncherComponents import Component, Type, components, icon_paths
from .client.keyClient import start_client

components.append(
    Component(
        "Kirby's Epic Yarn",
        component_type=Type.CLIENT,
        func=start_client,
        game_name="Kirby's Epic Yarn",
        supports_uri=False,
        #description="Launch the Kirby Epic Yarn Client."
    )
)
