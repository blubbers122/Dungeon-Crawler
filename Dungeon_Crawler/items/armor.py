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
    def __init__(self, name, value, amount, description):
        super().__init__(name, value, amount, description)
        self.resistance = armorBank[name]["resistance"]

    equippable = True
