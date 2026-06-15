from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Location
from . import items
if TYPE_CHECKING:
    from .world import KirbyYarnWorld

startLocation = ['Start']

quiltySquareDoorLocations = [
    'Patch Castle Goal'
]
grassLandDoorLocations = [
    'Fountain Gardens Goal', 'Flower Fields Goal', 'Rainbow Falls Goal',
    'Big-Bean Vine Goal', 'Mole Hole Goal', 'Weird Woods Goal',
    'Fangora Goal',
]
hotLandDoorLocations = [
    'Pyramid Sands Goal', 'Lava Landing Goal', 'Cool Cave Goal',
    'Dino Jungle Goal', 'Temper Temple Goal', 'Dusk Dunes Goal',
    'Hot Wings Goal',
]
treatLandDoorLocations = [
    'Toy Tracks Goal', 'Mushroom Run Goal', 'Sweets Park Goal',
    'Melody Town Goal', 'Cocoa Station Goal', 'Dark Manor Goal',
    'Squashini Goal',
]
waterLandDoorLocations = [
    'Splash Beach Goal', 'Blub-Blub Ocean Goal', 'Secret Island Goal',
    'Deep-Dive Deep Goal', 'Boom Boatyard Goal', 'Fossil Reef Goal',
    'Capamari Goal',
]
snowLandDoorLocations = [
    'Snowy Fields Goal', 'Cozy Cabin Goal', 'Mt. Slide Goal',
    'Frosty Wheel Goal', 'Frigid Fjords Goal', 'Evergreen Lift Goal',
    'King Dedede Goal',
]
spaceLandDoorLocations = [
    'Future City Goal', 'Tube Town Goal', 'Mysterious UFO Goal',
    'Stellar Way Goal', 'Moon Base Goal', 'Outer Rings Goal',
    'Meta Knight Goal'
]
dreamLandDoorLocations = [
    "Whispy's Forest Goal", 'Tempest Towers Goal', 'Cloud Palace Goal',
    'Castle Dedede Goal', 'Meta Melon Isle Goal', 'Battleship Halberd Goal',
]

quiltySquareChestLocations = [
    'Patch Castle 1', 'Patch Castle 2', 'Patch Castle 3',
]
grassLandChestLocations = [
    'Fountain Gardens 1', 'Fountain Gardens 2', 'Fountain Gardens 3',
    'Flower Fields 1', 'Flower Fields 2', 'Flower Fields 3',
    'Rainbow Falls 1', 'Rainbow Falls 2', 'Rainbow Falls 3',
    'Big-Bean Vine 1', 'Big-Bean Vine 2', 'Big-Bean Vine 3',
    'Mole Hole 1', 'Mole Hole 2', 'Mole Hole 3',
    'Weird Woods 1', 'Weird Woods 2', 'Weird Woods 3',
    'Fangora Disk',
]
hotLandChestLocations = [
    'Pyramid Sands 1', 'Pyramid Sands 2', 'Pyramid Sands 3',
    'Lava Landing 1', 'Lava Landing 2', 'Lava Landing 3',
    'Cool Cave 1', 'Cool Cave 2', 'Cool Cave 3',
    'Dino Jungle 1', 'Dino Jungle 2', 'Dino Jungle 3',
    'Temper Temple 1', 'Temper Temple 2', 'Temper Temple 3',
    'Dusk Dunes 1', 'Dusk Dunes 2', 'Dusk Dunes 3',
    'Hot Wings Disk',
]
treatLandChestLocations = [
    'Toy Tracks 1', 'Toy Tracks 2', 'Toy Tracks 3',
    'Mushroom Run 1', 'Mushroom Run 2', 'Mushroom Run 3',
    'Sweets Park 1', 'Sweets Park 2', 'Sweets Park 3',
    'Melody Town 1', 'Melody Town 2', 'Melody Town 3',
    'Cocoa Station 1', 'Cocoa Station 2', 'Cocoa Station 3',
    'Dark Manor 1', 'Dark Manor 2', 'Dark Manor 3',
    'Squashini Disk',
]
waterLandChestLocations = [
    'Splash Beach 1', 'Splash Beach 2', 'Splash Beach 3',
    'Blub-Blub Ocean 1', 'Blub-Blub Ocean 2', 'Blub-Blub Ocean 3',
    'Secret Island 1', 'Secret Island 2', 'Secret Island 3',
    'Deep-Dive Deep 1', 'Deep-Dive Deep 2', 'Deep-Dive Deep 3',
    'Boom Boatyard 1', 'Boom Boatyard 2', 'Boom Boatyard 3',
    'Fossil Reef 1', 'Fossil Reef 2', 'Fossil Reef 3',
    'Capamari Disk',
]
snowLandChestLocations = [
    'Snowy Fields 1', 'Snowy Fields 2', 'Snowy Fields 3',
    'Cozy Cabin 1', 'Cozy Cabin 2', 'Cozy Cabin 3',
    'Mt. Slide 1', 'Mt. Slide 2', 'Mt. Slide 3',
    'Frosty Wheel 1', 'Frosty Wheel 2', 'Frosty Wheel 3',
    'Frigid Fjords 1', 'Frigid Fjords 2', 'Frigid Fjords 3',
    'Evergreen Lift 1', 'Evergreen Lift 2', 'Evergreen Lift 3',
    'King Dedede Disk',
]
spaceLandChestLocations = [
    'Future City 1', 'Future City 2', 'Future City 3',
    'Tube Town 1', 'Tube Town 2', 'Tube Town 3',
    'Mysterious UFO 1', 'Mysterious UFO 2', 'Mysterious UFO 3',
    'Stellar Way 1', 'Stellar Way 2', 'Stellar Way 3',
    'Moon Base 1', 'Moon Base 2', 'Moon Base 3',
    'Outer Rings 1', 'Outer Rings 2', 'Outer Rings 3',
    'Meta Knight Disk',
]
dreamLandChestLocations = [
    "Whispy's Forest 1", "Whispy's Forest 2", "Whispy's Forest 3",
    'Tempest Towers 1', 'Tempest Towers 2', 'Tempest Towers 3',
    'Cloud Palace 1', 'Cloud Palace 2', 'Cloud Palace 3',
    'Castle Dedede 1', 'Castle Dedede 2', 'Castle Dedede 3',
    'Meta Melon Isle 1', 'Meta Melon Isle 2', 'Meta Melon Isle 3',
    'Battleship Halberd 1', 'Battleship Halberd 2', 'Battleship Halberd 3',
    #'Yin-Yarn Disk 1', Yin-Yarn Disk 2', Yin-Yarn Disk 3'
]

doorLocations = (
    quiltySquareDoorLocations + grassLandDoorLocations + hotLandDoorLocations +
    treatLandDoorLocations + waterLandDoorLocations + snowLandDoorLocations +
    spaceLandDoorLocations + dreamLandDoorLocations
)
chestLocations = (
    quiltySquareChestLocations + grassLandChestLocations + hotLandChestLocations +
    treatLandChestLocations + waterLandChestLocations + snowLandChestLocations +
    spaceLandChestLocations + dreamLandChestLocations
)

allLocations = startLocation + doorLocations + chestLocations

location_name_to_id = {name: id for
                       id, name in enumerate(allLocations, 1)}

class KirbyYarnLocation(Location):
    game: str = "Kirby's Epic Yarn"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: location_name_to_id[location_name] for location_name in location_names}

def create_all_locations(world: KirbyYarnWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: KirbyYarnWorld) -> None:
    quilty_square = world.get_region("Quilty Square")
    grass_land = world.get_region("Grass Land")
    hot_land = world.get_region("Hot Land")
    treat_land = world.get_region("Treat Land")
    water_land = world.get_region("Water Land")
    snow_land = world.get_region("Snow Land")
    space_land = world.get_region("Space Land")
    dream_land = world.get_region("Dream Land")

    rQuiltySquareLocations = get_location_names_with_ids(list(startLocation+quiltySquareDoorLocations+quiltySquareChestLocations))
    quilty_square.add_locations(rQuiltySquareLocations)

    rGrassLandLocations = get_location_names_with_ids(list(grassLandDoorLocations+grassLandChestLocations))
    grass_land.add_locations(rGrassLandLocations)

    rHotLandLocations = get_location_names_with_ids(list(hotLandDoorLocations+hotLandChestLocations))
    hot_land.add_locations(rHotLandLocations)

    rTreatLandLocations = get_location_names_with_ids(list(treatLandDoorLocations+treatLandChestLocations))
    treat_land.add_locations(rTreatLandLocations)

    rWaterLandLocations = get_location_names_with_ids(list(waterLandDoorLocations+waterLandChestLocations))
    water_land.add_locations(rWaterLandLocations)

    rSnowLandLocations = get_location_names_with_ids(list(snowLandDoorLocations+snowLandChestLocations))
    snow_land.add_locations(rSnowLandLocations)

    rSpaceLandLocations = get_location_names_with_ids(list(spaceLandDoorLocations+spaceLandChestLocations))
    space_land.add_locations(rSpaceLandLocations)

    rDreamLandLocations = get_location_names_with_ids(list(dreamLandDoorLocations+dreamLandChestLocations))
    dream_land.add_locations(rDreamLandLocations)

def create_events(world: KirbyYarnWorld) -> None:
    dream_land = world.get_region("Dream Land")
    dream_land.add_event(
        "Yin-Yarn Defeated", "Victory", location_type=KirbyYarnLocation, item_type=items.KirbyYarnItem
    )