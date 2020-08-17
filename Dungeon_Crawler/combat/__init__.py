from ..display import printCentered, printLine, printMenu
from random import randint
from time import sleep
import pyinputplus as pyip

class Combat:
    def __init__(self, player, enemy):
        self.start(player, enemy)

    def start(self, player, enemy):
        printCentered("FIGHT", "#")
        sleep(1)
        print(enemy.name + " approaches")

        # player goes first if you are faster and saw the enemy before the fight
        if player.speed > enemy.speed and enemy.detected:
            print("you rush into battle")
            count = 0
        # enemy goes first
        else:
            if enemy.detected:
                print("%s was too fast!" % enemy.name)
            else:
                print("%s snuck up on me!" % enemy.name)
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
                            player.loot(enemy)
                        del enemy

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
