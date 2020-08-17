from ..items import Item

armorBank = {
    # "none": {"value": 0,
    #          "resistance": 0},
    "leather armor": {"value": 26,
                      "resistance": 2,
                      "description": "A worn set of leather."},
    "chainmail armor": {"value": 36,
                        "resistance": 3,
                        "description": "Chainy."},
    "dark cloak": {"value": 18,
                   "resistance": 1,
                   "description": "I won't need extra protection if they can't see me!"},
}

class Armor(Item):
    def __init__(self, name=None, amount=None):
        super().__init__(name, amount)
        self.value = armorBank[self.name]["value"]
        self.description = armorBank[self.name]["description"]
        self.resistance = armorBank[self.name]["resistance"]

    types = list(armorBank.keys())

    maxFindableStack = 1

    equippable = True
