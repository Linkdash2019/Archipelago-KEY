from worlds.AutoWorld import WebWorld
from BaseClasses import Tutorial

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
