from ..player import Player

class Warrior(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.defense = 3

    damageMult = 1.5

    weapon = "iron sword"
    armor = "chainmail armor"

class Ranger(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.defense = 2

    damageMult = 1.8

    weapon = "short bow"
    armor = "leather armor"

# give much better luck than the others
class Rogue(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.defense = 1

    damageMult = 1.2

    weapon = "iron dagger"
    armor = "dark cloak"

class Deprived(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.defense = 0

    damageMult = 1
    weapon = ""
    armor = ""
    inventory = {}
