class Enemy:

    inventory = {
        "gold coin": 5
    }

    # TODO: edit this code to display enemy inv
    def displayInventory(self):
        print("Enter item name to take, enter 'b' to go back or enter 'a' to take all")
        for key, item in self.inventory.items():
            print("%s %s" % (item, key))
        while True:
            choice = pyip.inputCustom(lambda x: x if x in self.inventory or x == "b" or x == "a" else "r", prompt=">")
            if choice != "r":
                break
        if choice == "b":
            return



    defense = 0
