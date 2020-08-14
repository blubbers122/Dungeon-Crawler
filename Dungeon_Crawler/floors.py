floorNames = ["The Caves", "The Archives", "The Slime Caverns", "The Dungeon", "The Catacombs"]

class Floor:
    def __init__():
        pass

    level = 1
    eventsAllowed = None
    dangerMultiplier = 1
    name = "the caves"

    currentRoom = None

    def nextFloor(self):
        self.level += 1
        dangerMultiplier += .15
