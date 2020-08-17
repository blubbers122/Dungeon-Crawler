from random import randint

class Item:
    def __init__(self, name=None, amount=None):
        self.usable = False
        if not name:
            self.name = self.chooseItem()
            self.amount = self.chooseAmount()
        else:
            self.name = name
            self.amount = amount

    def chooseItem(self):
        return self.types[randint(0, len(self.types) - 1)]

    def chooseAmount(self):
        return 1 if self.maxFindableStack == 1 else randint(1, self.maxFindableStack)

    def addToInventory(self):
        print(self.name + " was added to your inventory")

    def itemStrings(self):
        return [self.description, "Value: %s" % self.value, "Quantity: %s" % self.amount]

    def __repr__(self):
        itemString = "%s %s(s) " % (self.amount, self.name)
        return itemString
