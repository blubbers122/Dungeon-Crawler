containerBank = {
    "chest": {"rarity": 5,
                "max items": 5,
                "item class weights": {} # will store the chance of item class to appear inside
                },
    "pot": {"rarity": 2,
                "max items": 2},
    "weapon rack": {"rarity": 2,
                "max items": 2}
}

class Container:
    def __init__(self):
        self.fillInventory()

    def fillInventory(self):
        pass

    inventory = []
    name = "chest"
