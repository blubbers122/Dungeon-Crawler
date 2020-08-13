from ..items import Item

class Misc(Item):
    def __init__(self, name, value, amount, description):
        super().__init__(name, value, amount, description)

    equippable = False
