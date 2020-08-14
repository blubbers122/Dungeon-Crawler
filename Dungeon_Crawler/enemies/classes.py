from . import Enemy
from random import randint
from ..items import treasure

class Skeleton(Enemy):
    def __init__(self):
        self.health = 3 + randint(-2, 2)
        self.inventory = [treasure.Treasure("gold coin", 5 + randint(-4, 4))]

    name = "skeleton"
    strength = 5
    speed = 2
    agression = 7


class Bat(Enemy):
    def __init__(self):
        self.health = 3 + randint(-2, 2)
        self.inventory = [treasure.Treasure("gold coin", 5 + randint(-4, 4))]
    # TODO: make noise
    # chance leech health from you?
    name = "bat"

    strength = 3
    speed = 5
    agression = 3


class Boss(Enemy):
    pass
