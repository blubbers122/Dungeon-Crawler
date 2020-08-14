from ..battle_entity import Entity
from .controls import *
from ..items import treasure, weapons, armor
from ..display import *
from pyinputplus import inputChoice

class Player(Entity):
    def __init__(self, strength, speed, name):
        self.strength = strength
        self.speed = speed
        self.name = name
        self.inventory = [treasure.Treasure("gold coin", 50), weapons.Weapon("metal lance", 1), armor.Armor("leather armor", 1)]
        self.defense = 0
        self.damageMult = 0
        self.health = 100
        self.hunger = 100
        self.perception = 5
        self.equipped = {
            "weapon": None,
            "armor": None
        }

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

    def addToInventory(self, itemToAdd):
        # search inventory for existing stack of item
        for item in self.inventory:
            if item.name == itemToAdd.name:
                item.amount += itemToAdd.amount
                print("%s added to inventory." % itemToAdd.name)
                return

        # adds new stack to inv
        self.inventory.append(itemToAdd)
        print("%s added to inventory." % itemToAdd.name)

    def equip(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        if item.__class__.__name__ == "Armor":
            oldArmor = self.equipped["armor"]
            if oldArmor:
                self.addToInventory(oldArmor)
            self.equipped["armor"] = item
            self.defense = item.resistance
        else:
            oldWeapon = self.equipped["weapon"]
            if oldWeapon:
                self.addToInventory(oldWeapon)
            self.equipped["weapon"] = item
            self.damageMult = item.damageMult

    def unequip(self, toolType):
        pass

    def consumeItem(self, item):
        for effect in item.effects:
            print(effect)
        if item.amount > 1:
            item.amount -= 1
        else:
            self.inventory.remove(item)

    def loot(self, container):
        while True:
            inventoryMenu = container.inventoryStrings()
            validChoices = [str(x) for x in range(1, len(container.inventory) + 1)]
            validChoices.append("b")

            printMenu(inventoryMenu, topText=container.name)
            if len(validChoices) == 1:
                break
            printCentered("*enter the number to take item or press 'b' to return*")
            choice = inputChoice(validChoices, prompt=">")
            if choice == "b":
                break

            item = container.inventory[int(choice) - 1]
            self.addToInventory(item)
            container.inventory.remove(item)

    def equipment(self):
        weapon = self.equipped["weapon"]
        armor = self.equipped["armor"]
        return "Weapon: %s" % (weapon.name if weapon else "none"), "Armor: %s" % (armor.name if armor else "none")

    def status(self):
        attributes = ["Health: %s" % self.health,
        "Strength: %s" % self.strength,
        "Defense: %s" % self.defense,
        "Speed: %s" % self.speed,
        "Hunger: %s / 100" % self.hunger]
        return attributes
