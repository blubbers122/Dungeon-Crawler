from .containers import Container
from random import randint
from .util import chooseFromProbability

roomTypes = ["the room", "an abandoned camp", "a dark cellar", "a cell"]


class Room:
    def __init__(self):
        self.name = roomTypes[randint(0, len(roomTypes) - 1)]
        self.size = randint(2, 5)
        self.entranceMessage = "" # what will be printed when you enter the room
        self.danger = 5
        self.fortune = 5
        self.neighborCount = randint(1, 3)
        self.neighbors = []
        self.containerCount = randint(1, 5)
        self.containers = []
        self.enemyCount = randint(1, self.size)
        self.enemies = []
        self.current = False

    def generateContainers(self, floor):
        for i in range(self.containerCount):
            container = Container()
            self.containers.append(container)

    def generateEnemies(self, floor):
        filled = []
        for i in range(self.enemyCount):
            location = randint(0, self.size)
            if location in filled: return

            # picks enemy type from probablities
            enemyType = chooseFromProbability(floor.enemyWeights)

            # creates the enemy at current location
            enemy = floor.enemiesAllowed[enemyType](location)
            self.enemies.append(enemy)

            filled.append(location)

    def generateNeighbors(self):
        for i in range(self.neighborCount):
            room = Room()
            self.neighbors.append(room)

    def __repr__(self):
        return "%s\nFortune: %s\nSize: %s\nNeighbors: %s\nContainers: %s\nEnemies: %s" % (self.name, self.fortune, self.size, self.neighborCount, self.containerCount, self.enemyCount)
