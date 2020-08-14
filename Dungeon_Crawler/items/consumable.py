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
    def __init__(self, name, value, amount, description):
        super().__init__(name, value, amount, description)
        self.effects = consumableBank[name]["effects"]
        self.value = consumableBank[name]["value"]
        self.description = consumableBank[name]["description"]

    equippable = False
