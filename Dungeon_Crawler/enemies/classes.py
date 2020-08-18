from . import Enemy
from random import randint
from ..items import treasure

class Skeleton(Enemy):
    def __init__(self, roomLocation):
        super().__init__(roomLocation)
        self.health = 3 + randint(-2, 2)
        self.inventory = [treasure.Treasure("gold coin", 10 + randint(-4, 4))]

    name = "skeleton"
    strength = 5
    speed = 3
    aggression = 7


class Bat(Enemy):
    def __init__(self, roomLocation):
        super().__init__(roomLocation)
        self.health = 20 + randint(-2, 2)
        self.inventory = [treasure.Treasure("gold coin", 5 + randint(-4, 4))]
    # TODO: make noise
    # chance leech health from you?
    name = "bat"

    stealth = 2
    perception = 2
    strength = 3
    speed = 6
    aggression = 10


class Slime(Enemy):
    def __init__(self, roomLocation):
        super().__init__(roomLocation)
        self.health = 3 + randint(-2, 2)
        self.inventory = [treasure.Treasure("gold coin", 5 + randint(-4, 4))]

    name = "slime"

    strength = 5
    speed = 2
    aggression = 4

    damageType = "poison"

class Boss(Enemy):
    pass
