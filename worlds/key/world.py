from BaseClasses import ItemClassification, Region
import typing

from worlds.AutoWorld import World

from .options import KirbyYarnOptions  # the options we defined earlier
from .items import KirbyYarnItem, nothingItem, doorItems, chestItems  # data used below to add items to the World
from .locations import KirbyYarnLocation, startLocation, doorLocations, chestLocations  # same as above

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
    def generate_early(self) -> None:
        # read player options to world instance
        pass

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        menu_region.add_locations(startLocation, KirbyYarnLocation)
        menu_region.add_locations(doorLocations, KirbyYarnLocation)
        menu_region.add_locations(chestLocations, KirbyYarnLocation)
        self.multiworld.regions.append(menu_region)

    def create_item(self, item: str) -> KirbyYarnItem:
        # this is called when AP wants to create an item by name (for plando, start inventory, item links) or when you call it from your own code
        return KirbyYarnItem(item, ItemClassification.progression, self.item_name_to_id[item], self.player)

    def create_items(self) -> None:
        for item in map(self.create_item, (doorItems+chestItems)):
            self.multiworld.itempool.append(item)

        # itempool and number of locations should match up.
        # If this is not the case we want to fill the itempool with junk.
        junk = 0  # calculate this based on player options
        self.multiworld.itempool += [self.create_item(nothingItem) for _ in range(junk)]

