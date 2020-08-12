from ..battle_entity import Entity
from .controls import *

class Player(Entity):
    def __init__(self, strength, speed, name):
        super().__init__(strength, speed)
        self.name = name

    inventory = {"gold coin": 50}
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

    def displayInventory(self):
        print("inventory")
        """
        for key, item in self.inventory.items():
            print("%s %s" % (item, key))
        while True:
            choice = pyip.inputCustom(lambda x: x if x in self.inventory or x == "b" else "r", prompt=">")
            if choice != "r":
                break

        if choice != "b":
            choiceAmount = self.inventory[choice]
            if choice in armorBank:
                choiceDesc = choice + ": " + armorBank[choice]["description"]
                print(choiceDesc)
                if pyip.inputMenu(["e", "b"], prompt=">Press 'e' to equip or 'b' to return: ") == "e":
                    self.equip(choice)
            elif choice in weaponBank:
                choiceDesc = choice + ": " + weaponBank[choice]["description"]
                print(choiceDesc)
                if pyip.inputMenu(["e", "b"], prompt=">Press 'e' to equip or 'b' to return: ") == "e":
                    self.equip(choice)
            else:
                choiceDesc = choice + ": " + treasureBank[choice]["description"]
                print(choiceDesc)
                """

    def equip(self, itemName):
        # remove item from bag
        """
        self.inventory[itemName] -= 1
        if self.inventory[itemName] < 1:
            del self.inventory[itemName]

        if itemName in armorBank:
            oldArmor = self.armor
            if oldArmor != "none":
                print("removing " + self.armor)
                self.addToInventory(oldArmor)
            print("equipping " + itemName, end="")
            for x in range(3):
                time.sleep(.5)
                print(".", end="" if x != 2 else "\n")
            self.armor = itemName
            self.defense = armorBank[itemName]["resistance"]
        else:
            oldWeapon = self.weapon
            if oldWeapon != "fists":
                print("removing " + self.weapon)
                self.addToInventory(oldWeapon)
            print("equipping " + itemName, end="")
            for x in range(3):
                time.sleep(.5)
                print(".", end="" if x != 2 else "\n")
            self.weapon = itemName

    def equipment(self):
        if self.weapon != "fists":
            print("Weapon: %s raises damage by %s percent." % (self.weapon, weaponBank[self.weapon]["damageMult"] * 100))
        else:
            print("Weapon: Just my bare hands.")
        if self.armor != "none":
            print("Armor: %s raises defense by %s points." % (self.armor, armorBank[self.armor]["resistance"]))
        else:
            print("Armor: No armor.")
            """

    def addToInventory(self, item):
        self.inventory[item] = self.inventory.get(item, 0)
        self.inventory[item] += 1

    def status(self):
        print("Health: %s" % self.health)
        print("Strength: %s" % self.strength)
        print("Defense: %s" % self.defense)
        print("Speed: %s" % self.speed)
        print("Hunger: %s / 100" % self.hunger)
