from ..items import Item

treasureBank = {
    "gold coin": {"value": 1,
             "description": "A shiny golden coin!"},
    "ruby": {"value": 100,
             "description": "A red, reflective precioius gem. I should sell this!"},
    "sapphire": {"value": 200,
            "description": "Blue, bright, and brilliant."},
    "emerald": {"value": 300,
            "description": "As green as grass, yet much harder to cut."},
    "diamond": {"value": 500,
            "description": "Wow, nice find!"}
}

class Treasure(Item):
    def __init__(self, name=None, amount=None):
        super().__init__(name, amount)
        self.description = treasureBank[self.name]["description"]
        self.value = treasureBank[self.name]["value"]

    types = list(treasureBank.keys())

    maxFindableStack = 10

    equippable = False
