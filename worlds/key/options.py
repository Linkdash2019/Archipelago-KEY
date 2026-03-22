from Options import Toggle, Range, Choice, PerGameCommonOptions, DefaultOnToggle
from dataclasses import dataclass

class ShuffleDoors(DefaultOnToggle):
    """Adds level doors and goals to the pool"""
    display_name = "Shuffle Doors"

class ShuffleChests(Toggle):
    """Adds chests, apartment items, and soundtracks to the pool"""
    display_name = "Shuffle Chests"

@dataclass
class KirbyYarnOptions(PerGameCommonOptions):
    shuffle_doors: ShuffleDoors
    shuffle_chests: ShuffleChests
