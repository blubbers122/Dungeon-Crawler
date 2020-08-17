from .containers import Container
from random import randint
from .enemies.classes import Bat

roomTypes = {}

class Room:
    def __init__(self):
        self.name = "the room"
        self.size = 5
        self.danger = 5
        self.fortune = 5
        self.neighborCount = randint(1, 3)
        self.neighbors = []
        self.containerCount = randint(1, 5)
        self.containers = []
        self.enemyCount = randint(1, self.size)
        self.enemies = []
        self.current = False

    def generateContainers(self):
        for i in range(self.containerCount):
            container = Container()
            self.containers.append(container)

    def generateEnemies(self):
        filled = []
        for i in range(self.enemyCount):
            #TODO: randomize enemy type to an extent

            
            location = randint(0, self.size)
            if location in filled: return

            enemy = Bat(location)
            self.enemies.append(enemy)
            filled.append(location)

    def generateNeighbors(self):
        for i in range(self.neighborCount):
            room = Room()
            self.neighbors.append(room)

    def __repr__(self):
        return "%s\nFortune: %s\nSize: %s\nNeighbors: %s\nContainers: %s\nEnemies: %s" % (self.name, self.fortune, self.size, self.neighborCount, self.containerCount, self.enemyCount)
