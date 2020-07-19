import pyinputplus as pyip
import time
import random

treasureBank = {
    "gold coin": {"value": 1,
             "description": "A shiny golden coin!"},
    "ruby": {"value": 50,
             "description": "A red, reflective precioius gem. I should sell this!"}
}

weaponBank = {
    "fists": {"value": 0,
              "damageMult": 1},
    "iron sword": {"value": 16,
                   "damageMult": 1.5,
                   "description": "An iron longsword, with a slightly rusted blade."},
    "metal lance": {"value": 22,
                    "damageMult": 1.6,
                    "description": "This is heavy, who knows if I can use it effectively."},
    "iron dagger": {"value": 9,
                   "damageMult": 1.2,
                   "description": "Well, it's a little better than a butter knife I guess..."},
    "short bow": {"value": 27,
                   "damageMult": 1.8,
                   "description": "A quick bow."},
}

# TODO: change resistance to DefenseMult
armorBank = {
    "none": {"value": 0,
             "resistance": 0},
    "leather armor": {"value": 26,
                      "resistance": 2,
                      "description": "A worn set of leather."},
    "chainmail armor": {"value": 36,
                        "resistance": 3,
                        "description": "Chainy."},
    "dark cloak": {"value": 18,
                   "resistance": 1,
                   "description": "I won't need extra protection if they can't see me!"},
}


class Person:
    def __init__(self, name, strength, speed):
        self.name = name
        self.strength = strength
        self.speed = speed

    def attack(self):
        print(self.name + " hits their opponent.")

    def person(self):
        print("I am person")


class Player(Person):
    def __init__(self, name, strength, speed, inventory):
        super().__init__(name, strength, speed)
        self.inventory = inventory

    weapon = "fists"
    armor = "none"
    damageMult = weaponBank[weapon]["damageMult"]
    defense = armorBank[armor]["resistance"]
    health = 100
    hunger = 100

    def displayInventory(self):
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

    def equip(self, itemName):
        # remove item from bag
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

    def addToInventory(self, item):
        self.inventory[item] = self.inventory.get(item, 0)
        self.inventory[item] += 1

    def status(self):
        print("Health: %s" % self.health)
        print("Strength: %s" % self.strength)
        print("Defense: %s" % self.defense)
        print("Speed: %s" % self.speed)
        print("Hunger: %s / 100" % self.hunger)

    def equipment(self):
        if self.weapon != "fists":
            print("Weapon: %s raises damage by %s percent." % (self.weapon, weaponBank[self.weapon]["damageMult"] * 100))
        else:
            print("Weapon: Just my bare hands.")
        if self.armor != "none":
            print("Armor: %s raises defense by %s points." % (self.armor, armorBank[self.armor]["resistance"]))
        else:
            print("Armor: No armor.")


class Warrior(Player):
    weapon = "iron sword"
    armor = "chainmail armor"
    defense = armorBank[armor]["resistance"]


class Ranger(Player):
    weapon = "short bow"
    armor = "leather armor"
    defense = armorBank[armor]["resistance"]

# give much better luck than the others
class Rogue(Player):
    weapon = "iron dagger"
    armor = "dark cloak"
    defense = armorBank[armor]["resistance"]


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


class Skeleton(Enemy):
    name = "skeleton"
    health = 40 + random.randint(-4, 4)
    strength = 5
    speed = 2


class Bat(Enemy):
    # TODO: make noise
    name = "bat"
    health = 20 + random.randint(-2, 2)
    strength = 3
    speed = 5


class Boss(Enemy):
    pass


class Item:
    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description

    def addToInventory(self):
        print(self.name + " was added to your inventory")


class Misc(Item):  # things like torches, keys, rope
    pass

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

class Consumable(Item):
    pass