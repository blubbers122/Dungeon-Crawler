from ..player import Player

class Warrior(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.defense = 3

    damageMult = 1.5
    className = "Warrior"

    weapon = "iron sword"
    armor = "chainmail armor"

class Ranger(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.defense = 2

    damageMult = 1.8
    className = "ranger"

    weapon = "short bow"
    armor = "leather armor"

# give much better luck than the others
class Rogue(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.defense = 1

    damageMult = 1.2
    className = "Rogue"

    weapon = "iron dagger"
    armor = "dark cloak"

class Deprived(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.defense = 0

    damageMult = 1
    className = "Deprived"

    weapon = ""
    armor = ""

class Mage(Player):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed, name)
        self.defense = 0
        
    className = "Mage"

    weapon = ""
    armor = ""
