from ..battle_entity import Entity
from .controls import *
from ..items import treasure

class Player(Entity):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed)
        self.name = name
        self.inventory = [treasure.Treasure("gold coin", 1, 50, "A shiny golden coin!")]


    weapon = ""
    armor = ""
    health = 100
    hunger = 100

    moveSet = {
        "i": showPlayerInventory,
        "c": showControls,
        "s": showPlayerStatus,
        "r": runAway,
        "f": fight,
        "q": quitGame,
        "l": lookAround,
        "e": endTurn
        }

    def inventoryStrings(self):
        return ["%s: %s %s" % (index + 1, item.amount, item.name) for index, item in enumerate(self.inventory)]


    def equip(self, itemName):
        pass

    def equipment(self):
        return "Weapon: %s" % self.weapon, "Armor: %s" % self.armor


    def addToInventory(self, item):
        self.inventory[item] = self.inventory.get(item, 0)
        self.inventory[item] += 1

    def status(self):
        attributes = ["Health: %s" % self.health,
        "Strength: %s" % self.strength,
        "Defense: %s" % self.defense,
        "Speed: %s" % self.speed,
        "Hunger: %s / 100" % self.hunger]
        return attributes
