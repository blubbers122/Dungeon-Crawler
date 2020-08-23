from .the_caves import enemyBank, enemies

floorNames = ["The Caves", "The Archives", "The Slime Caverns", "The Dungeon", "The Catacombs"]

class Floor:
    def __init__(self):

        self.level = 1
        self.eventsAllowed = None
        self.enemyWeights = enemyBank
        self.enemiesAllowed = enemies
        self.dangerMultiplier = 1
        self.name = floorNames[0]

        self.currentRoom = None

    def nextFloor(self):
        self.level += 1
        self.dangerMultiplier += .15
