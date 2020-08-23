from ..battle_entity import Entity

class Enemy(Entity):
    def __init__(self, roomLocation):
        self.roomLocation = roomLocation
        self.detected = False

    perception = 5

    def __repr__(self):
        return "%s at location %s." % (self.name, self.roomLocation)

    stealth = 0

    damageMult = 1

    defense = 0

    conservativity = 5 # will have an effect on how recklessly they fight
