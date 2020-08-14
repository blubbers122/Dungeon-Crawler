from .items import *
from random import randint
from .battle_entity import Entity

containerBank = {
    "chest": {"rarity": 5,
                "max items": 5,
                "item class weights": {} # will store the chance of item class to appear inside
                },
    "pot": {"rarity": 2,
                "max items": 2},
    "weapon rack": {"rarity": 2,
                "max items": 2}
}

containerTypes = list(containerBank.keys())


class Container(Entity):
    def __init__(self):
        self.name = containerTypes[randint(0, len(containerTypes) - 1)]
        self.itemCount = randint(1, containerBank[self.name]["max items"])
        self.rarity = containerBank[self.name]["rarity"]
        self.inventory = []
        self.fillInventory()
        self.visibility = randint(1, 10)

        self.discoveryMessage = "You found a %s!" % self.name

    def fillInventory(self):
        for i in range(self.itemCount):
            item = Item("gold coin", randint(1, 13))
            self.inventory.append(item)

    def __repr__(self):
         aboutContainer = "%s with %s items with a visibility of %s and a rarity of %s\n" % (self.name, self.itemCount, self.visibility, self.rarity)
         aboutContainer += "holding: "
         for item in self.inventory:
             aboutContainer += str(item)
         return aboutContainer
