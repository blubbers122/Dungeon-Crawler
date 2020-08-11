from ..player import Player

class Warrior(Player):
    weapon = "iron sword"
    armor = "chainmail armor"

class Ranger(Player):
    weapon = "short bow"
    armor = "leather armor"

# give much better luck than the others
class Rogue(Player):
    weapon = "iron dagger"
    armor = "dark cloak"

class Deprived(Player):
    weapon = ""
    armor = ""
    inventory = {}
