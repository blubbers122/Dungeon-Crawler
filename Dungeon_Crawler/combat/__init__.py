from ..display import printCentered, printLine, printMenu
from random import randint
from time import sleep
import pyinputplus as pyip

class Combat:
    def __init__(self, player, enemy):
        self.start(player, enemy)

    def start(self, player, enemy):
        printCentered("FIGHT", "#")
        if player.speed > enemy.speed:
            count = 0
        else:
            count = 1
        while True:
            if count % 2 == 0:
                print("%s: %s hp\n%s: %s hp" % (enemy.name, enemy.health, player.name, player.health))
                printCentered("*press 'f' to attack or 'r' to run.*")
                move = pyip.inputMenu(["f", "r"], prompt=">")
                if move == "f":
                    rawDamage = player.attack(enemy)
                    print("%s hits %s and deals %s damage!" % (player.name, enemy.name, rawDamage))
                    printLine("-")
                    sleep(1)
                    if enemy.health <= 0:
                        print(enemy.name + " was defeated!\n")
                        printLine("#")
                        # TODO: add looting here
                        print("loot %s? " % enemy.name)
                        if pyip.inputYesNo(">") == "yes":
                            self.lootEnemy(player, enemy)

                        printLine("-")
                        break
                else:
                    print("you run away")
                    printLine("-")
                    break
            else:
                rawDamage = enemy.attack(player)
                print("%s strikes you and deals %s damage!" % (enemy.name, rawDamage))
                printLine("-")
                sleep(1)
                if player.health <= 0:
                    print("You died!")
                    exit()
            count += 1
        player.hunger -= count

    def lootEnemy(self, player, enemy):
        while True:
            inventoryMenu = enemy.inventoryStrings()
            validChoices = [str(x) for x in range(1, len(enemy.inventory) + 1)]
            validChoices.append("b")
            printMenu(inventoryMenu, topText=enemy.name)
            if len(validChoices) == 1:
                break
            printCentered("*enter the number to take item or press 'b' to return*")
            choice = pyip.inputChoice(validChoices, prompt=">")
            if choice == "b":
                break

            item = enemy.inventory[int(choice) - 1]
            player.addToInventory(item)
            enemy.inventory.remove(item)
