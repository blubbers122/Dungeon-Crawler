from ..items import Item

consumableBank = {
    "health potion": {
        "effects": {"health restore": 20},
        "value": 35,
        "description": "a small glass vial holding a powerful red liquid."
    },
    "charred meat": {
        "effects": {"health restore": 5,
                    "satiate": 25},
        "value": 35,
        "description": "the outside is pretty blackened, but not too much to be inedible."
    }
}


class Consumable(Item):
    def __init__(self, name=None, amount=None):
        super().__init__(name, amount)
        self.effects = consumableBank[self.name]["effects"]
        self.value = consumableBank[self.name]["value"]
        self.description = consumableBank[self.name]["description"]

    types = list(consumableBank.keys())


    equippable = False
