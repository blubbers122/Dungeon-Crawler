from random import randint

class Item:
    def __init__(self, name=None, amount=None):
        if not name:
            print('not name')
            self.name = self.chooseItem()
            self.amount = self.chooseAmount()
        else:
            self.name = name
            self.amount = amount

    def chooseItem(self):
        print("i chose " + self.types[randint(0, len(self.types) - 1)])
        return self.types[randint(0, len(self.types) - 1)]

    def chooseAmount(self):
        return randint(1, 3)

    def addToInventory(self):
        print(self.name + " was added to your inventory")

    def itemStrings(self):
        return [self.description, "Value: %s" % self.value, "Quantity: %s" % self.amount]

    def __repr__(self):
        itemString = "%s %s(s) " % (self.amount, self.name)
        return itemString
