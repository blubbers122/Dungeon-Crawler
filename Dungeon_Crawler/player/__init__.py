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
        self.damageMult = 1
        self.health = 100
        self.hunger = 100
        self.roomLocation = 0
        self.currentRoom = None
        self.detected = False # True if an enemy sees you
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
        "e": endTurn,
        "m": map
        }

    def addToInventory(self, itemToAdd):
        # search inventory for existing stack of item
        for item in self.inventory:
            if item.name == itemToAdd.name:
                item.amount += itemToAdd.amount
                print("%s added to inventory." % itemToAdd)
                return

        # adds new stack to inv
        self.inventory.append(itemToAdd)
        print("%s added to inventory." % itemToAdd)

    def equip(self, item):
        # removes the item from inventory if the stack has only
        # one of the item, otherwise it decrements the stack
        if item in self.inventory:
            if item.amount == 1:
                self.inventory.remove(item)
            else:
                item.amount -= 1
        if item.__class__.__name__ == "Armor":
            oldArmor = self.equipped["armor"]
            if oldArmor:
                self.addToInventory(oldArmor)
                print("you replaced your %s you had equipped with the %s" % (oldArmor.name, item.name))
            self.equipped["armor"] = item
            self.defense = item.resistance
        else:
            oldWeapon = self.equipped["weapon"]
            if oldWeapon:
                self.addToInventory(oldWeapon)
                print("you replaced your %s you had equipped with the %s" % (oldWeapon.name, item.name))
            self.equipped["weapon"] = item
            self.damageMult = item.damageMult

    def unequip(self, toolType):
        pass

    def dropItem(self, item):
        self.inventory.remove(item)
        print("you dropped the %s" % item)

    def consumeItem(self, item):
        for effect, strength in item.effects.items():
            if effect == "health restore":
                if self.health + strength < 100:
                    self.health += strength
                    print("%s's health was restored by %s points." % (self.name, strength))
                else:
                     self.health = 100
                     print("health fully restored")
            elif effect == "satiate":
                print("you feel less full after eating the %s" % item.name)
                if self.hunger + strength < 100:
                    self.hunger += strength
                else:
                    self.hunger = 100
                    print("you are stuffed")
        if item.amount > 1:
            item.amount -= 1
        else:
            self.inventory.remove(item)

    def loot(self, container):
        while True:
            inventoryMenu = container.inventoryStrings()
            validChoices = [str(x) for x in range(1, len(container.inventory) + 1)]
            validChoices.extend(["b", "a"])

            printMenu(inventoryMenu, topText=container.name)
            # if everything has been looted, exit
            if len(validChoices) == 2:
                break
            printCentered("*enter the number to take item, press 'a' to loot all, or 'b' to return*")
            choice = inputChoice(validChoices, prompt=">")
            # exit loot menu option
            if choice == "b":
                break
            # loot all
            elif choice == "a":
                for item in container.inventory:
                    self.addToInventory(item)
                break
            # loot one item
            else:
                item = container.inventory[int(choice) - 1]
                self.addToInventory(item)
                container.inventory.remove(item)

    # returns text describing player's equipment
    def equipment(self):
        weapon = self.equipped["weapon"]
        armor = self.equipped["armor"]
        return "Weapon: %s" % (weapon.name if weapon else "none"), "Armor: %s" % (armor.name if armor else "none")

    # returns multiple text lines describing the player's current status
    def status(self):
        attributes = ["Health: %s" % self.health,
        "Strength: %s" % self.strength,
        "Defense: %s" % self.defense,
        "Speed: %s" % self.speed,
        "Hunger: %s / 100" % self.hunger]
        return attributes
