from ..display import printCentered, printLine
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
                print("press 'f' to attack or 'r' to run.")
                move = pyip.inputMenu(["f", "r"], prompt=">")
                if move == "f":
                    rawDamage = player.strength * player.damageMult - enemy.defense + randint(-2, 2)
                    if rawDamage <= 0:
                        rawDamage = 1
                    enemy.health -= rawDamage
                    print("%s hits %s with %s and deals %s damage!\n" % (player.name, enemy.name, player.weapon, rawDamage))
                    sleep(1)
                    if enemy.health <= 0:
                        print(enemy.name + " was defeated!\n")
                        printLine("#")
                        # TODO: add looting here
                        if pyip.inputYesNo(">loot %s? " % enemy.name) == "yes":
                            printCentered(enemy.name, "-")
                            print(enemy.inventory)
                            printLine("-")
                        break
                else:
                    print("you run away")
                    break
            else:
                rawDamage = enemy.strength - player.defense + randint(-2, 2)
                if rawDamage <= 0:
                    rawDamage = 1
                player.health -= rawDamage
                print("%s strikes you and deals %s damage!\n" % (enemy.name, rawDamage))
                sleep(1)
                if player.health <= 0:
                    print("You died!")
                    exit()
            count += 1
        player.hunger -= count
