import pyinputplus as pyip
import time

treasureBank = {
    "gold coin": {"value": 1,
             "description": "A shiny golden coin!"},
    "ruby": {"value": 50,
             "description": "A red, reflective precioius gem. I should sell this!"}
}

weaponBank = {
    "iron sword": {"value": 16,
                   "damageMult": 1.5,
                   "description": "An iron longsword, with a slightly rusted blade."},
    "metal lance": {"value": 22,
                    "damageMult": 1.6,
                    "description": "This is heavy, who knows if I can use it effectively."},

}

armorBank = {
    "leather armor": {"value": 26,
                      "resistance": 1,
                      "description": "A worn set of leather."},
    "chainmail armor": {"value": 36,
                        "resistance": 2,
                        "description": "A worn set of leather."},
}

banks = [treasureBank, weaponBank, armorBank]


class Person:
    def __init__(self, name, health, strength, defense, speed):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed

    def attack(self):
        print(self.name + " hits their opponent.")

    def person(self):
        print("I am person")


class Player(Person):
    # change inventory to keep only right values
    inventory = {
        1: ["gold coin", 1],
        2: ["ruby", 1],
        3: ["iron sword", 1],
        4: ["leather armor", 2],
        5: ["metal lance", 1],
        6: ["chainmail armor", 1]
    }
    weapon = "fists"
    armor = "none"
    hunger = 100
    totalItems = len(inventory.keys())

    def player(self):
        print("I am player " + self.name)

    def displayInventory(self):
        for key, item in self.inventory.items():
            print("%s: %s %s" % (key, item[1], item[0]))
        choice = pyip.inputInt(">", min=0, max=self.totalItems)
        if choice != 0:
            choiceName = self.inventory[choice][0]
            choiceAmount = self.inventory[choice][1]
            for bank in banks:
                if choiceName in bank:
                    choiceDesc = choiceName + ": " + bank[choiceName]["description"]
                    if bank == armorBank or bank == weaponBank:
                        print(choiceDesc)
                        if pyip.inputMenu(["e", "b"], prompt="Press 'e' to equip or 'b' to return") == "e":
                            self.equip(choiceName)
                    else:
                        print(choiceDesc)

    def equip(self, itemName):
        for key, val in self.inventory.items():
            if val[0] == itemName:
                val[1] -= 1
                if val[1] < 1:
                    del self.inventory[key]
                    break

        if itemName in armorBank:
            oldArmor = self.armor
            if oldArmor != "none":
                print("removing " + itemName)
                self.addToInventory(oldArmor)
            print("equipping " + itemName, end="")
            for x in range(3):
                time.sleep(.5)
                print(".", end="")
            self.armor = itemName
        else:
            oldWeapon = self.weapon
            if oldWeapon != "fists":
                print("removing " + self.weapon)
                self.addToInventory(oldWeapon)
            print("equipping " + itemName)
            for x in range(3):
                time.sleep(.5)
                print(".", end="")
            self.weapon = itemName

    def addToInventory(self, item):
        for key, value in self.inventory.items():  # search inventory for existing entry of item
            if value[0] == item:
                self.inventory[key][1] += 1



    def equip(self, itemName):
        for key, val in self.inventory.items():
            if val[0] == itemName:
                val[1] -= 1
                if val[1] < 1:
                    del self.inventory[key]
                    break


    def status(self):
        print("Health: %s" % self.health)
        print("Strength: %s" % self.strength)
        print("Defense: %s" % self.defense)
        print("Speed: %s" % self.speed)
        print("Hunger: %s" % self.hunger)

    def equipment(self):
        if self.weapon != "fists":
            print("Weapon: %s raises damage by %s percent." % (self.weapon, weaponBank[self.weapon]["damageMult"] * 100))
        if self.armor != "none":
            print("Armor: %s raises defense by %s percent." % (self.armor, armorBank[self.armor]["resistance"] * 100))
        if self.weapon == "fists":
            print("Weapon: Just my bare hands.")
        if self.armor == "none":
            print("Armor: No armor, just the clothes on my back.")








# TODO: add player sub-classes (eg. Knight, Ranger, Wizard)

class Enemy(Person):
    def enemy(self):
        print("I am enemy " + self.name)


class Skeleton(Enemy):
    def enemy(self):
        print("I'm enemy skeley " + self.name)


class Bat(Enemy):
    pass


class Boss(Enemy):
    pass


class Item:
    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description

    def addToInventory(self):
        print(self.name + " was added to your inventory")


class Treasure(Item):
    pass


class Weapon(Item):
    def __init__(self, name, value, description, damageMult):
        super().__init__(name, value, description)
        self.damageMult = damageMult


class Armor(Item):
    def __init__(self, name, value, description, resistance):
        super().__init__(name, value, description)
        self.resistance = resistance