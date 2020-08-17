floorNames = ["The Caves", "The Archives", "The Slime Caverns", "The Dungeon", "The Catacombs"]

class Floor:
    def __init__(self):
        pass

    level = 1
    eventsAllowed = None
    dangerMultiplier = 1
    name = floorNames[0]

    currentRoom = None

    def nextFloor(self):
        self.level += 1
        dangerMultiplier += .15
