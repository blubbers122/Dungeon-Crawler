from ..player import Player
from ..items import weapons, armor

class Warrior(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.equip(weapons.Weapon("iron sword", 1))
        self.equip(armor.Armor("chainmail armor", 1))
        self.stealth = 2
        self.perception = 3
        self.currentPerception = 3

    className = "Warrior"

class Ranger(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.equip(weapons.Weapon("short bow", 1))
        self.equip(armor.Armor("leather armor", 1))
        self.stealth = 4
        self.perception = 6
        self.currentPerception = 6

    className = "Ranger"

# give much better luck than the others
class Rogue(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.equip(weapons.Weapon("iron dagger", 1))
        self.equip(armor.Armor("dark cloak", 1))
        self.stealth = 6
        self.perception = 5
        self.currentPerception = 5

    className = "Rogue"

class Deprived(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)

    className = "Deprived"

class Mage(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)

    className = "Mage"
