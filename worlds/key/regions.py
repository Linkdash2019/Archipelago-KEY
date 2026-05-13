from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region
if TYPE_CHECKING:
    from worlds.key import KirbyYarnWorld


def create_and_connect_regions(world: KirbyYarnWorld):
    create_regions(world)
    connect_regions(world)

def create_regions(world: KirbyYarnWorld):
    quilty_square = Region("Quilty Square", world.player, world.multiworld)
    grass_land = Region("Grass Land", world.player, world.multiworld)
    hot_land = Region("Hot Land", world.player, world.multiworld)
    treat_land = Region("Treat Land", world.player, world.multiworld)
    water_land = Region("Water Land", world.player, world.multiworld)
    snow_land = Region("Snow Land", world.player, world.multiworld)
    space_land = Region("Space Land", world.player, world.multiworld)
    dream_land = Region("Dream Land", world.player, world.multiworld)

    regions = [quilty_square, grass_land, hot_land, treat_land, water_land, snow_land, space_land, dream_land]

    world.multiworld.regions += regions

def connect_regions(world: KirbyYarnWorld):
    quilty_square = world.get_region("Quilty Square")
    grass_land = world.get_region("Grass Land")
    hot_land = world.get_region("Hot Land")
    treat_land = world.get_region("Treat Land")
    water_land = world.get_region("Water Land")
    snow_land = world.get_region("Snow Land")
    space_land = world.get_region("Space Land")
    dream_land = world.get_region("Dream Land")

    world.origin_region_name = "Quilty Square"

    quilty_square.connect(grass_land, "Quilty Square to Grass Land")
    grass_land.connect(hot_land, "Grass Land to Hot Land")
    hot_land.connect(treat_land, "Hot Land to Treat Land")
    treat_land.connect(water_land, "Treat Land to Water Land")
    water_land.connect(snow_land, "Water Land to Snow Land")
    snow_land.connect(space_land, "Snow Land to Space Land")
    space_land.connect(quilty_square, "Space Land to Quilty Square")
    quilty_square.connect(dream_land, "Quilty Square to Dream Land")