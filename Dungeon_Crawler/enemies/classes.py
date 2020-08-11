from . import Enemy
from random import randint

class Skeleton(Enemy):
    name = "skeleton"
    health = 40 + randint(-4, 4)
    strength = 5
    speed = 2


class Bat(Enemy):
    # TODO: make noise
    name = "bat"
    health = 20 + randint(-2, 2)
    strength = 3
    speed = 5


class Boss(Enemy):
    pass
