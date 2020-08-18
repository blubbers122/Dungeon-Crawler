from ..items import Item

miscBank = {
    "torch": {
        "value": 5,
        "description": "this will be very useful if I find a way to light it."
    }
}



class Misc(Item):
    def __init__(self, name=None, amount=None):
        super().__init__(name, amount)
        self.value = miscBank[self.name]["value"]
        self.description = miscBank[self.name]["description"]

    types = list(miscBank.keys())

    maxFindableStack = 3

    equippable = False
