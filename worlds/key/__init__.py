import settings
import typing
from .options import KirbyYarnOptions  # the options we defined earlier
from .items import KirbyYarnItem, nothingItem, doorItems, chestItems  # data used below to add items to the World
from .locations import KirbyYarnLocation, startLocation, doorLocations, chestLocations  # same as above
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, icon_paths, launch

def run_client(*args: str) -> None:
    """
    Launch the Kirby Epic Yarn client.

    :param *args: Variable length argument list passed to the client.
    """
    print("Running the Kirby Epic Yarn Client")
    from .KEYClient import main

    launch(main, name="KirbyEpicYarnClient", args=args)

class KirbyYarnWebWorld(WebWorld):
    rich_text_options_doc = False #https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
    theme = "partyTime"
    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Kirby's Epic Yarn randomizer connected to an Archipelago Multiworld.",
            "English",
            "multiworld_en.md",
            "setup/en",
            ["Linkdash2019"]
        )
    ]
    bug_report_page = 'https://github.com/Linkdash2019/Archipelago-KEY/issues'

class KirbyYarnWorld(World):
    """
    Help Kirby save both Patch Land and Dream Land.
    """

    game = "Kirby's Epic Yarn"  # name of the game/world
    options_dataclass = KirbyYarnOptions  # options the player can set
    options: KirbyYarnOptions  # typing hints for option results
    settings: typing.ClassVar[KirbyYarnOptions]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    base_id = 1234
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which items exist.
    item_name_to_id = {name: id for
                       id, name in enumerate(nothingItem+doorItems+chestItems, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(startLocation|doorLocations|chestLocations, base_id)}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
    }

components.append(
    Component(
        "Kirby's Epic Yarn",
        func=run_client,
        component_type=Type.CLIENT,
        file_identifier=SuffixIdentifier(".apkey"),
    )
)