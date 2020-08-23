from .items import armor, consumable, misc, treasure, weapons
from random import randint
from .battle_entity import Entity
from .util import chooseFromProbability

containerBank = {
    "chest": {"rarity": 5,
                "max items": 5,
                "item class weights": {
                    "armor": 20,
                    "consumable": 10,
                    "misc": 10,
                    "treasure": 40,
                    "weapon": 20
                } # will store the chance of item class to appear inside
                },
    "pot": {"rarity": 2,
                "max items": 2,
                "item class weights": {
                    "armor": 0,
                    "consumable": 20,
                    "misc": 20,
                    "treasure": 60,
                    "weapon": 0
                }},
    "weapon rack": {"rarity": 2,
                "max items": 2,
                "item class weights": {
                    "armor": 0,
                    "consumable": 0,
                    "misc": 0,
                    "treasure": 0,
                    "weapon": 100
                }}
}

containerTypes = list(containerBank.keys())


itemClasses = {
    "armor": armor.Armor,
    "consumable": consumable.Consumable,
    "misc": misc.Misc,
    "treasure": treasure.Treasure,
    "weapon": weapons.Weapon
}

itemTypes = list(itemClasses.keys())

class Container(Entity):
    def __init__(self):
        self.name = containerTypes[randint(0, len(containerTypes) - 1)]
        self.itemCount = randint(1, containerBank[self.name]["max items"])
        self.rarity = containerBank[self.name]["rarity"]
        self.inventory = []
        self.itemClassWeights = containerBank[self.name]["item class weights"]
        self.fillInventory()
        self.visibility = randint(1, 10)


        self.discoveryMessage = "You found a %s!" % self.name

    def fillInventory(self):
        for i in range(self.itemCount):
            type = chooseFromProbability(self.itemClassWeights)
            item = itemClasses[type]()
            # won't append duplicate items to container
            if item.name not in [x.name for x in self.inventory]:
                self.inventory.append(item)

    def __repr__(self):
         aboutContainer = "%s with %s items with a visibility of %s and a rarity of %s\n" % (self.name, self.itemCount, self.visibility, self.rarity)
         aboutContainer += "holding: "
         for item in self.inventory:
             aboutContainer += str(item)
         return aboutContainer
