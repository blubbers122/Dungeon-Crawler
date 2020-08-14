from ..items import Item

armorBank = {
    "none": {"value": 0,
             "resistance": 0},
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
    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.value = armorBank[name]["value"]
        self.description = armorBank[name]["description"]
        self.resistance = armorBank[name]["resistance"]

    equippable = True
