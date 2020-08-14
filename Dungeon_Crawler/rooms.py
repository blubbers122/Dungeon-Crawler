from .containers import Container
from random import randint

roomTypes = {}

class Room:
    def __init__(self):
        self.size = 5
        self.danger = 5
        self.fortune = 5
        self.neighborCount = randint(1, 3)
        self.neighbors = []
        self.containerCount = randint(1, 5)
        self.containers = []
        self.current = False

    def generateContainers(self):
        for i in range(self.containerCount):
            container = Container()
            self.containers.append(container)

    def generateNeighbors(self):
        for i in range(self.neighborCount):
            room = Room()
            self.neighbors.append(room)
