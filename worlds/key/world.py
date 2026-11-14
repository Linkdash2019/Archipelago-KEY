from worlds.AutoWorld import World
from . import items, locations, regions, rules, web_world
from . import options as KirbyYarnOptions
class KirbyYarnWorld(World):
    """
    Help Kirby save both Patch Land and Dream Land from Yin-Yarns knitting needles.
    """

    game = "Kirby's Epic Yarn"  # name of the game/world
    web = web_world.KirbyYarnWebWorld()
    options_dataclass = KirbyYarnOptions.KirbyYarnOptions  # options the player can set
    options: KirbyYarnOptions.KirbyYarnOptions  # typing hints for option results
    topology_present = True  # show path to required location checks in spoiler

    # The following two dicts are required for the generation to know which items exist.
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    # There is always one region that the generator starts from & assumes you can always go back to.
    origin_region_name = "Quilty Square"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.KirbyYarnItem:
        # this is called when AP wants to create an item by name (for plando, start inventory, item links) or when you call it from your own code
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

