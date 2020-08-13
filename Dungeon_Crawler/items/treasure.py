from ..items import Item

treasureBank = {
    "gold coin": {"value": 1,
             "description": "A shiny golden coin!"},
    "ruby": {"value": 50,
             "description": "A red, reflective precioius gem. I should sell this!"}
}

class Treasure(Item):
    def __init__(self, name, value, amount, description):
        super().__init__(name, value, amount, description)

    equippable = False
