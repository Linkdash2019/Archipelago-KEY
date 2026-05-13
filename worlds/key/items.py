from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import KirbyYarnWorld

nothingItem = ['Nothing']

doorItems = [
    'Patch Castle', #Quilty Square
    'Fountain Gardens', 'Flower Fields',   'Rainbow Falls',  'Big-Bean Vine', 'Mole Hole',       'Weird Woods',   #Grass Land
    'Pyramid Sands',    'Lava Landing',    'Cool Cave',      'Dino Jungle',    'Temper Temple',   'Dusk Dunes',    #Hot Land
    'Toy Tracks',       'Mushroom Run',    'Sweets Park',    'Melody Town',    'Cocoa Station',   'Dark Manor',    #Treat Land
    'Splash Beach',     'Blub-Blub Ocean', 'Secret Island',  'Deep-Dive Deep', 'Boom Boatyard',   'Fossil Reef',   #Water Land
    'Snowy Fields',     'Cozy Cabin',      'Mt. Slide',      'Frosty Wheel',   'Frigid Fjords',   'Evergreen Lift',#Snow Land
    'Future City',      'Tube Town',       'Mysterious UFO', 'Stellar Way',    'Moon Base',       'Outer Rings',   #Space Land
    "Whispy's Forest",  'Tempest Towers',  'Cloud Palace',   'Castle_Dedede' , 'Meta Melon Isle', 'Battleship Halberd',#Dream Land
    'Fangora', 'Hot Wings', 'Squashini', 'Capamari', 'King Dedede', 'Meta Knight', 'Yin-Yarn' #Bosses
]

chestItems = [
    #Quilty Square
    "Chandelier","King's Throne","Patch Castle Soundtrack",
    #Grass Land
    "Flower Sofa", "Fountain", "Fountain Gardens Soundtrack",
    "Flower Clock", "Frog Umbrella Stand", "Flower Fields Soundtrack",
    "Rainbow Arch", "Outdoor Bath", "Rainbow Falls Soundtrack",
    "Lattice", "Cloud Pillow", "Big-Bean Vine Soundtrack",
    "Carrot Dresser", "Tree-Stump Bed", "Mole Hole Soundtrack",
    "Telescope", "Log Cake", "Weird Woods Soundtrack",
    #Hot Land
    "Camel Sofa", "Cactus Juice", "Pyramid Sands Soundtrack",
    "Stone Lamp", "Cartoon Meat", "Lava Landing Soundtrack",
    "Crystal", "Frog Mirror", "Cool Cave Soundtrack",
    "Bronto Slide", "Torch", "Dino Jungle Soundtrack",
    "Pyramid", "Camel Pillow", "Quilty Square Soundtrack",
    "Magic Carpet", "Hourglass", "Dusk Dunes Soundtrack",
    #Treat Land
    "Stuffed Bear", "Tin Robot", "Toy Tracks Soundtrack",
    "Mushroom Bed", "Mushroom Lamp", "Mushroom Run Soundtrack",
    "Donut Pillow", "Dessert Dresser", "Grass Land Soundtrack",
    "Toy Piano", "Clef Tree", "Melody Town Soundtrack",
    "Choco Ottoman", "Chocolate Bar", "Hot Land Soundtrack",
    "Ghost-in-a-Box", "Pumpkin", "Dark Manor Soundtrack",
    #Water Land
    "Sun Clock", "Moon Clock", "Secret Island Soundtrack",
    "Jellyfish Light", "Aquarium", "Blub-Blub Ocean Soundtrack",
    "Treasure Rug", "Totem Pole", "Splash Beach Soundtrack",
    "Dangler Light", "Mast", "Deep-Dive Deep Soundtrack",
    "Pirate Ship", "Treasure Chest", "Treat Land Soundtrack",
    "Anemone Sofa", "Fossil", "Water Land Soundtrack",
    #Snow Land
    "Big Bear Bed", "Penguin Mirror", "Snowy Fields Soundtrack",
    "Fireplace", "Chimney", "Cozy Cabin Soundtrack",
    "Knit-Cap Sofa", "Snowman", "Mt. Slide Soundtrack",
    "Snow Clock", "Snow Globe", "Frosty Wheel Soundtrack",
    "Penguin Chest", "Sleigh", "Snow Land Soundtrack",
    "Holiday Tree", "Star Wreath", "Quilty Court Soundtrack",
    #Space Land
    "Space Monitor", "Space Table", "Future City Soundtrack",
    "Digital Clock", "Circuitry Rug", "Tube Town Soundtrack",
    "Communicator", "Space Food", "Space Land Soundtrack",
    "Robot Bed", "Star Candy", "Stellar Way Soundtrack",
    "Cosmic Bin", "Porthole", "Tankbot Soundtrack",
    "Saturn Stand", "Saturn Donuts", "Outer Rings Soundtrack",
    #Dream Land
    "Whispy Woods", "Apple Table", "Green Greens Soundtrack",
    "Bookcase", "Pancakes", "Butter Building Soundtrack",
    "Cloud Rug", "Bubbly Soda", "Bubbly Clouds Soundtrack",
    "Castle Dedede", "Dedede's Robe", "Gourment Race Soundtrack",
    "Palm Chair", "Ice Cream", "Ice Cream Island Soundtrack",
    "Galaxia Sword", "Knight Helmet", "Halberd Soundtrack",
    #Bosses
    "Fangora Soundtrack", "Hot Wings Soundtrack", "Squashini Soundtrack",
    "Capamari Soundtrack", "King Dedede Soundtrack", "Meta Knight Soundtrack"#,
    #"Yin-Yarn Soundtrack", "Dream Land Soundtrack", "Staff Credits Soundtrack"
]

combinedItems = nothingItem+doorItems+chestItems

item_name_to_id = {name: id for
                       id, name in enumerate(nothingItem+doorItems+chestItems, 1)}

default_item_classification = {item: ItemClassification.progression for item in doorItems}
default_item_classification |= {item: ItemClassification.deprioritized for item in (nothingItem+chestItems)}
default_item_classification |= {ItemClassification.progression: "Yin-Yarn"}


class KirbyYarnItem(Item):
    game = "Kirby's Epic Yarn"

def get_random_filler_item_name(world: KirbyYarnWorld):
    return "Nothing"

def create_item_with_correct_classification(world: KirbyYarnWorld, name: str) -> KirbyYarnItem:
    classification = default_item_classification[name]
    return KirbyYarnItem(name, classification, item_name_to_id[name], world.player)

def create_all_items(world: KirbyYarnWorld) -> None:
    for item in map(world.create_item, (doorItems + chestItems)):
        world.multiworld.itempool.append(item)

    # itempool and number of locations should match up.
    # If this is not the case we want to fill the itempool with junk.
    junk = 0  # calculate this based on player options
    world.multiworld.itempool += [KirbyYarnWorld.create_item(world, "Nothing") for _ in range(junk)]