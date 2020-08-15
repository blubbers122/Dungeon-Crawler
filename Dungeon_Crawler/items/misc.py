from ..items import Item

miscBank = {
    "misc1": {
        "value": 5
    }
}



class Misc(Item):
    def __init__(self, name=None, amount=None):
        super().__init__(name, amount)
        self.value = miscBank[self.name]["value"]

    types = list(miscBank.keys())



    equippable = False
