
class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def addToInventory(self):
        print(self.name + " was added to your inventory")

    def itemStrings(self):
        return [self.description, "Value: %s" % self.value, "Quantity: %s" % self.amount]

    def __repr__(self):
        itemString = "%s %s(s) " % (self.amount, self.name)
        return itemString
