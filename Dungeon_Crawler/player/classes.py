from ..player import Player
from ..items import weapons, armor

class Warrior(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.equip(weapons.Weapon("iron sword", 1))
        self.equip(armor.Armor("chainmail armor", 1))

    className = "Warrior"

class Ranger(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.equip(weapons.Weapon("short bow", 1))
        self.equip(armor.Armor("leather armor", 1))

    className = "ranger"

# give much better luck than the others
class Rogue(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.equip(weapons.Weapon("iron dagger", 1))
        self.equip(armor.Armor("dark cloak", 1))

    className = "Rogue"

class Deprived(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)

    className = "Deprived"

class Mage(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)

    className = "Mage"
