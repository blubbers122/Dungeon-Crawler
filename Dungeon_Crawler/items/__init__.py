
class Item:
    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description

    def addToInventory(self):
        print(self.name + " was added to your inventory")
