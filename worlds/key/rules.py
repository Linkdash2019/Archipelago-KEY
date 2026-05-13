from __future__ import annotations
from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .locations import *
if TYPE_CHECKING:
    from .world import KirbyYarnWorld


def set_all_rules(world: KirbyYarnWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: KirbyYarnWorld) -> None:
    """
    quiltySquare_to_dreamLand = world.get_entrance("Quilty Square to Dream Land")
    dreamLandUnlocked = Has("Magic Sock")
    world.set_rule(quiltySquare_to_dreamLand, dreamLandUnlocked)
    """
    pass

def set_all_location_rules(world: KirbyYarnWorld) -> None:
    quilty_square = world.get_region("Quilty Square")
    grass_land = world.get_region("Grass Land")
    hot_land = world.get_region("Hot Land")
    treat_land = world.get_region("Treat Land")
    water_land = world.get_region("Water Land")
    snow_land = world.get_region("Snow Land")
    space_land = world.get_region("Space Land")
    dream_land = world.get_region("Dream Land")

    canEnterLvl1_1 = Has("Patch Castle")

    canEnterLvl2_1 = Has("Fountain Gardens")
    canEnterLvl2_2 = Has("Flower Fields")
    canEnterLvl2_3 = Has("Rainbow Falls")
    canEnterLvl2_4 = Has("Big-Bean Vine")
    canEnterLvl2_Boss = Has("Fangora")
    canEnterLvl2_5 = Has("Mole Hole")
    canEnterLvl2_6 = Has("Weird Woods")

    canEnterLvl3_1 = Has("Pyramid Sands")
    canEnterLvl3_2 = Has("Lava Landing")
    canEnterLvl3_3 = Has("Cool Cave")
    canEnterLvl3_4 = Has("Dino Jungle")
    canEnterLvl3_Boss = Has("Hot Wings")
    canEnterLvl3_5 = Has("Temper Temple")
    canEnterLvl3_6 = Has("Dusk Dunes")

    canEnterLvl4_1 = Has("Toy Tracks")
    canEnterLvl4_2 = Has("Mushroom Run")
    canEnterLvl4_3 = Has("Sweets Park")
    canEnterLvl4_4 = Has("Melody Town")
    canEnterLvl4_Boss = Has("Squashini")
    canEnterLvl4_5 = Has("Cocoa Station")
    canEnterLvl4_6 = Has("Dark Manor")

    canEnterLvl5_1 = Has("Splash Beach")
    canEnterLvl5_2 = Has("Blub-Blub Ocean")
    canEnterLvl5_3 = Has("Secret Island")
    canEnterLvl5_4 = Has("Deep-Dive Deep")
    canEnterLvl5_Boss = Has("Capamari")
    canEnterLvl5_5 = Has("Boom Boatyard")
    canEnterLvl5_6 = Has("Fossil Reef")

    canEnterLvl6_1 = Has("Snowy Fields")
    canEnterLvl6_2 = Has("Cozy Cabin")
    canEnterLvl6_3 = Has("Mt. Slide")
    canEnterLvl6_4 = Has("Frosty Wheel")
    canEnterLvl6_Boss = Has("King Dedede")
    canEnterLvl6_5 = Has("Frigid Fjords")
    canEnterLvl6_6 = Has("Evergreen Lift")

    canEnterLvl7_1 = Has("Future City")
    canEnterLvl7_2 = Has("Tube Town")
    canEnterLvl7_3 = Has("Mysterious UFO")
    canEnterLvl7_4 = Has("Stellar Way")
    canEnterLvl7_Boss = Has("Meta Knight")
    canEnterLvl7_5 = Has("Moon Base")
    canEnterLvl7_6 = Has("Outer Rings")

    canEnterLvl8_1 = Has("Whispy's Forest")
    canEnterLvl8_2 = Has("Tempest Towers")
    canEnterLvl8_3 = Has("Cloud Palace")
    canEnterLvl8_4 = Has("Castle_Dedede")
    canEnterLvl8_Boss = Has("Yin-Yarn")
    canEnterLvl8_5 = Has("Meta Melon Isle")
    canEnterLvl8_6 = Has("Battleship Halberd")

    world.set_rule(world.get_location("Patch Castle Goal"), canEnterLvl1_1)
    world.set_rule(world.get_location("Patch Castle 1"), canEnterLvl1_1)
    world.set_rule(world.get_location("Patch Castle 2"), canEnterLvl1_1)
    world.set_rule(world.get_location("Patch Castle 3"), canEnterLvl1_1)
    
    world.set_rule(world.get_location("Fountain Gardens Goal"), canEnterLvl2_1)
    world.set_rule(world.get_location("Fountain Gardens 1"), canEnterLvl2_1)
    world.set_rule(world.get_location("Fountain Gardens 2"), canEnterLvl2_1)
    world.set_rule(world.get_location("Fountain Gardens 3"), canEnterLvl2_1)
    
    world.set_rule(world.get_location("Flower Fields Goal"), canEnterLvl2_2)
    world.set_rule(world.get_location("Flower Fields 1"), canEnterLvl2_2)
    world.set_rule(world.get_location("Flower Fields 2"), canEnterLvl2_2)
    world.set_rule(world.get_location("Flower Fields 3"), canEnterLvl2_2)

    world.set_rule(world.get_location("Rainbow Falls Goal"), canEnterLvl2_3)
    world.set_rule(world.get_location("Rainbow Falls 1"), canEnterLvl2_3)
    world.set_rule(world.get_location("Rainbow Falls 2"), canEnterLvl2_3)
    world.set_rule(world.get_location("Rainbow Falls 3"), canEnterLvl2_3)

    world.set_rule(world.get_location("Big-Bean Vine Goal"), canEnterLvl2_4)
    world.set_rule(world.get_location("Big-Bean Vine 1"), canEnterLvl2_4)
    world.set_rule(world.get_location("Big-Bean Vine 2"), canEnterLvl2_4)
    world.set_rule(world.get_location("Big-Bean Vine 3"), canEnterLvl2_4)

    world.set_rule(world.get_location("Fangora Goal"), canEnterLvl2_Boss)
    world.set_rule(world.get_location("Fangora Disk"), canEnterLvl2_Boss)

    world.set_rule(world.get_location("Mole Hole Goal"), canEnterLvl2_5)
    world.set_rule(world.get_location("Mole Hole 1"), canEnterLvl2_5)
    world.set_rule(world.get_location("Mole Hole 2"), canEnterLvl2_5)
    world.set_rule(world.get_location("Mole Hole 3"), canEnterLvl2_5)

    world.set_rule(world.get_location("Weird Woods Goal"), canEnterLvl2_6)
    world.set_rule(world.get_location("Weird Woods 1"), canEnterLvl2_6)
    world.set_rule(world.get_location("Weird Woods 2"), canEnterLvl2_6)
    world.set_rule(world.get_location("Weird Woods 3"), canEnterLvl2_6)

    world.set_rule(world.get_location("Pyramid Sands Goal"), canEnterLvl3_1)
    world.set_rule(world.get_location("Pyramid Sands 1"), canEnterLvl3_1)
    world.set_rule(world.get_location("Pyramid Sands 2"), canEnterLvl3_1)
    world.set_rule(world.get_location("Pyramid Sands 3"), canEnterLvl3_1)

    world.set_rule(world.get_location("Lava Landing Goal"), canEnterLvl3_2)
    world.set_rule(world.get_location("Lava Landing 1"), canEnterLvl3_2)
    world.set_rule(world.get_location("Lava Landing 2"), canEnterLvl3_2)
    world.set_rule(world.get_location("Lava Landing 3"), canEnterLvl3_2)

    world.set_rule(world.get_location("Cool Cave Goal"), canEnterLvl3_3)
    world.set_rule(world.get_location("Cool Cave 1"), canEnterLvl3_3)
    world.set_rule(world.get_location("Cool Cave 2"), canEnterLvl3_3)
    world.set_rule(world.get_location("Cool Cave 3"), canEnterLvl3_3)

    world.set_rule(world.get_location("Dino Jungle Goal"), canEnterLvl3_4)
    world.set_rule(world.get_location("Dino Jungle 1"), canEnterLvl3_4)
    world.set_rule(world.get_location("Dino Jungle 2"), canEnterLvl3_4)
    world.set_rule(world.get_location("Dino Jungle 3"), canEnterLvl3_4)

    world.set_rule(world.get_location("Hot Wings Goal"), canEnterLvl3_Boss)
    world.set_rule(world.get_location("Hot Wings Disk"), canEnterLvl3_Boss)

    world.set_rule(world.get_location("Temper Temple Goal"), canEnterLvl3_5)
    world.set_rule(world.get_location("Temper Temple 1"), canEnterLvl3_5)
    world.set_rule(world.get_location("Temper Temple 2"), canEnterLvl3_5)
    world.set_rule(world.get_location("Temper Temple 3"), canEnterLvl3_5)

    world.set_rule(world.get_location("Dusk Dunes Goal"), canEnterLvl3_6)
    world.set_rule(world.get_location("Dusk Dunes 1"), canEnterLvl3_6)
    world.set_rule(world.get_location("Dusk Dunes 2"), canEnterLvl3_6)
    world.set_rule(world.get_location("Dusk Dunes 3"), canEnterLvl3_6)

    world.set_rule(world.get_location("Toy Tracks Goal"), canEnterLvl4_1)
    world.set_rule(world.get_location("Toy Tracks 1"), canEnterLvl4_1)
    world.set_rule(world.get_location("Toy Tracks 2"), canEnterLvl4_1)
    world.set_rule(world.get_location("Toy Tracks 3"), canEnterLvl4_1)

    world.set_rule(world.get_location("Mushroom Run Goal"), canEnterLvl4_2)
    world.set_rule(world.get_location("Mushroom Run 1"), canEnterLvl4_2)
    world.set_rule(world.get_location("Mushroom Run 2"), canEnterLvl4_2)
    world.set_rule(world.get_location("Mushroom Run 3"), canEnterLvl4_2)

    world.set_rule(world.get_location("Sweets Park Goal"), canEnterLvl4_3)
    world.set_rule(world.get_location("Sweets Park 1"), canEnterLvl4_3)
    world.set_rule(world.get_location("Sweets Park 2"), canEnterLvl4_3)
    world.set_rule(world.get_location("Sweets Park 3"), canEnterLvl4_3)

    world.set_rule(world.get_location("Melody Town Goal"), canEnterLvl4_4)
    world.set_rule(world.get_location("Melody Town 1"), canEnterLvl4_4)
    world.set_rule(world.get_location("Melody Town 2"), canEnterLvl4_4)
    world.set_rule(world.get_location("Melody Town 3"), canEnterLvl4_4)

    world.set_rule(world.get_location("Squashini Goal"), canEnterLvl4_Boss)
    world.set_rule(world.get_location("Squashini Disk"), canEnterLvl4_Boss)
    
    world.set_rule(world.get_location("Cocoa Station Goal"), canEnterLvl4_5)
    world.set_rule(world.get_location("Cocoa Station 1"), canEnterLvl4_5)
    world.set_rule(world.get_location("Cocoa Station 2"), canEnterLvl4_5)
    world.set_rule(world.get_location("Cocoa Station 3"), canEnterLvl4_5)

    world.set_rule(world.get_location("Dark Manor Goal"), canEnterLvl4_6)
    world.set_rule(world.get_location("Dark Manor 1"), canEnterLvl4_6)
    world.set_rule(world.get_location("Dark Manor 2"), canEnterLvl4_6)
    world.set_rule(world.get_location("Dark Manor 3"), canEnterLvl4_6)

    world.set_rule(world.get_location("Splash Beach Goal"), canEnterLvl5_1)
    world.set_rule(world.get_location("Splash Beach 1"), canEnterLvl5_1)
    world.set_rule(world.get_location("Splash Beach 2"), canEnterLvl5_1)
    world.set_rule(world.get_location("Splash Beach 3"), canEnterLvl5_1)

    world.set_rule(world.get_location("Blub-Blub Ocean Goal"), canEnterLvl5_2)
    world.set_rule(world.get_location("Blub-Blub Ocean 1"), canEnterLvl5_2)
    world.set_rule(world.get_location("Blub-Blub Ocean 2"), canEnterLvl5_2)
    world.set_rule(world.get_location("Blub-Blub Ocean 3"), canEnterLvl5_2)

    world.set_rule(world.get_location("Secret Island Goal"), canEnterLvl5_3)
    world.set_rule(world.get_location("Secret Island 1"), canEnterLvl5_3)
    world.set_rule(world.get_location("Secret Island 2"), canEnterLvl5_3)
    world.set_rule(world.get_location("Secret Island 3"), canEnterLvl5_3)

    world.set_rule(world.get_location("Deep-Dive Deep Goal"), canEnterLvl5_4)
    world.set_rule(world.get_location("Deep-Dive Deep 1"), canEnterLvl5_4)
    world.set_rule(world.get_location("Deep-Dive Deep 2"), canEnterLvl5_4)
    world.set_rule(world.get_location("Deep-Dive Deep 3"), canEnterLvl5_4)

    world.set_rule(world.get_location("Capamari Goal"), canEnterLvl5_Boss)
    world.set_rule(world.get_location("Capamari Disk"), canEnterLvl5_Boss)

    world.set_rule(world.get_location("Boom Boatyard Goal"), canEnterLvl5_5)
    world.set_rule(world.get_location("Boom Boatyard 1"), canEnterLvl5_5)
    world.set_rule(world.get_location("Boom Boatyard 2"), canEnterLvl5_5)
    world.set_rule(world.get_location("Boom Boatyard 3"), canEnterLvl5_5)

    world.set_rule(world.get_location("Fossil Reef Goal"), canEnterLvl5_6)
    world.set_rule(world.get_location("Fossil Reef 1"), canEnterLvl5_6)
    world.set_rule(world.get_location("Fossil Reef 2"), canEnterLvl5_6)
    world.set_rule(world.get_location("Fossil Reef 3"), canEnterLvl5_6)

    world.set_rule(world.get_location("Snowy Fields Goal"), canEnterLvl6_1)
    world.set_rule(world.get_location("Snowy Fields 1"), canEnterLvl6_1)
    world.set_rule(world.get_location("Snowy Fields 2"), canEnterLvl6_1)
    world.set_rule(world.get_location("Snowy Fields 3"), canEnterLvl6_1)

    world.set_rule(world.get_location("Cozy Cabin Goal"), canEnterLvl6_2)
    world.set_rule(world.get_location("Cozy Cabin 1"), canEnterLvl6_2)
    world.set_rule(world.get_location("Cozy Cabin 2"), canEnterLvl6_2)
    world.set_rule(world.get_location("Cozy Cabin 3"), canEnterLvl6_2)

    world.set_rule(world.get_location("Mt. Slide Goal"), canEnterLvl6_3)
    world.set_rule(world.get_location("Mt. Slide 1"), canEnterLvl6_3)
    world.set_rule(world.get_location("Mt. Slide 2"), canEnterLvl6_3)
    world.set_rule(world.get_location("Mt. Slide 3"), canEnterLvl6_3)

    world.set_rule(world.get_location("Frosty Wheel Goal"), canEnterLvl6_4)
    world.set_rule(world.get_location("Frosty Wheel 1"), canEnterLvl6_4)
    world.set_rule(world.get_location("Frosty Wheel 2"), canEnterLvl6_4)
    world.set_rule(world.get_location("Frosty Wheel 3"), canEnterLvl6_4)

    world.set_rule(world.get_location("King Dedede Goal"), canEnterLvl6_Boss)
    world.set_rule(world.get_location("King Dedede Disk"), canEnterLvl6_Boss)

    world.set_rule(world.get_location("Frigid Fjords Goal"), canEnterLvl6_5)
    world.set_rule(world.get_location("Frigid Fjords 1"), canEnterLvl6_5)
    world.set_rule(world.get_location("Frigid Fjords 2"), canEnterLvl6_5)
    world.set_rule(world.get_location("Frigid Fjords 3"), canEnterLvl6_5)

    world.set_rule(world.get_location("Evergreen Lift Goal"), canEnterLvl6_6)
    world.set_rule(world.get_location("Evergreen Lift 1"), canEnterLvl6_6)
    world.set_rule(world.get_location("Evergreen Lift 2"), canEnterLvl6_6)
    world.set_rule(world.get_location("Evergreen Lift 3"), canEnterLvl6_6)

    world.set_rule(world.get_location("Future City Goal"), canEnterLvl7_1)
    world.set_rule(world.get_location("Future City 1"), canEnterLvl7_1)
    world.set_rule(world.get_location("Future City 2"), canEnterLvl7_1)
    world.set_rule(world.get_location("Future City 3"), canEnterLvl7_1)

    world.set_rule(world.get_location("Tube Town Goal"), canEnterLvl7_2)
    world.set_rule(world.get_location("Tube Town 1"), canEnterLvl7_2)
    world.set_rule(world.get_location("Tube Town 2"), canEnterLvl7_2)
    world.set_rule(world.get_location("Tube Town 3"), canEnterLvl7_2)

    world.set_rule(world.get_location("Mysterious UFO Goal"), canEnterLvl7_3)
    world.set_rule(world.get_location("Mysterious UFO 1"), canEnterLvl7_3)
    world.set_rule(world.get_location("Mysterious UFO 2"), canEnterLvl7_3)
    world.set_rule(world.get_location("Mysterious UFO 3"), canEnterLvl7_3)

    world.set_rule(world.get_location("Stellar Way Goal"), canEnterLvl7_4)
    world.set_rule(world.get_location("Stellar Way 1"), canEnterLvl7_4)
    world.set_rule(world.get_location("Stellar Way 2"), canEnterLvl7_4)
    world.set_rule(world.get_location("Stellar Way 3"), canEnterLvl7_4)

    world.set_rule(world.get_location("Meta Knight Goal"), canEnterLvl7_Boss)
    world.set_rule(world.get_location("Meta Knight Disk"), canEnterLvl7_Boss)

    world.set_rule(world.get_location("Moon Base Goal"), canEnterLvl7_5)
    world.set_rule(world.get_location("Moon Base 1"), canEnterLvl7_5)
    world.set_rule(world.get_location("Moon Base 2"), canEnterLvl7_5)
    world.set_rule(world.get_location("Moon Base 3"), canEnterLvl7_5)

    world.set_rule(world.get_location("Outer Rings Goal"), canEnterLvl7_6)
    world.set_rule(world.get_location("Outer Rings 1"), canEnterLvl7_6)
    world.set_rule(world.get_location("Outer Rings 2"), canEnterLvl7_6)
    world.set_rule(world.get_location("Outer Rings 3"), canEnterLvl7_6)

    world.set_rule(world.get_location("Whispy's Forest Goal"), canEnterLvl8_1)
    world.set_rule(world.get_location("Whispy's Forest 1"), canEnterLvl8_1)
    world.set_rule(world.get_location("Whispy's Forest 2"), canEnterLvl8_1)
    world.set_rule(world.get_location("Whispy's Forest 3"), canEnterLvl8_1)

    world.set_rule(world.get_location("Tempest Towers Goal"), canEnterLvl8_2)
    world.set_rule(world.get_location("Tempest Towers 1"), canEnterLvl8_2)
    world.set_rule(world.get_location("Tempest Towers 2"), canEnterLvl8_2)
    world.set_rule(world.get_location("Tempest Towers 3"), canEnterLvl8_2)

    world.set_rule(world.get_location("Cloud Palace Goal"), canEnterLvl8_3)
    world.set_rule(world.get_location("Cloud Palace 1"), canEnterLvl8_3)
    world.set_rule(world.get_location("Cloud Palace 2"), canEnterLvl8_3)
    world.set_rule(world.get_location("Cloud Palace 3"), canEnterLvl8_3)

    world.set_rule(world.get_location("Castle Dedede Goal"), canEnterLvl8_4)
    world.set_rule(world.get_location("Castle Dedede 1"), canEnterLvl8_4)
    world.set_rule(world.get_location("Castle Dedede 2"), canEnterLvl8_4)
    world.set_rule(world.get_location("Castle Dedede 3"), canEnterLvl8_4)

    world.set_rule(world.get_location("Yin-Yarn Defeated"), canEnterLvl8_Boss)

    world.set_rule(world.get_location("Meta Melon Isle Goal"), canEnterLvl8_5)
    world.set_rule(world.get_location("Meta Melon Isle 1"), canEnterLvl8_5)
    world.set_rule(world.get_location("Meta Melon Isle 2"), canEnterLvl8_5)
    world.set_rule(world.get_location("Meta Melon Isle 3"), canEnterLvl8_5)

    world.set_rule(world.get_location("Battleship Halberd Goal"), canEnterLvl8_6)
    world.set_rule(world.get_location("Battleship Halberd 1"), canEnterLvl8_6)
    world.set_rule(world.get_location("Battleship Halberd 2"), canEnterLvl8_6)
    world.set_rule(world.get_location("Battleship Halberd 3"), canEnterLvl8_6)


def set_completion_condition(world: KirbyYarnWorld) -> None:
    world.set_completion_rule(HasAll("Yin-Yarn", "Victory"))