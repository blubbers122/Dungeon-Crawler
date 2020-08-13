
class Item:
    def __init__(self, name, value, amount, description):
        self.name = name
        self.value = value
        self.description = description
        self.amount = amount

    def addToInventory(self):
        print(self.name + " was added to your inventory")

    def itemStrings(self):
        return [self.description, "Value: %s" % self.value, "Quantity: %s" % self.amount]
