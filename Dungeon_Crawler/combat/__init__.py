from ..display import printCentered, printLine, printMenu
from random import randint
from time import sleep
import pyinputplus as pyip

class Combat:
    def __init__(self, player, enemy):
        self.turn = 1
        self.sneakAttack = None
        self.start(player, enemy)

    # returns turn offset 1 if enemy goes first and 1 otherwise
    def findFirstAttacker(self, player, enemy):
        # if you're in combat and dont see the enemy they hit first
        if not enemy.detected:
            print("a %s snuck up on me!" % enemy.name)
            self.sneakAttack = enemy
            return 1
        else:
            # if you see them and they don't see you, you go first
            if not player.detected:
                print("you were able to sneak up to the %s" % enemy.name)
                self.sneakAttack = player
                sleep(1)
                return 0
            # player goes first if you are faster and saw the enemy before the fight
            if player.speed > enemy.speed:
                print("you rush into battle")
                sleep(1)
                return 0
            # enemy goes first if it is faster
            elif enemy.speed > player.speed:
                print("%s was too fast!" % enemy.name)
                return 1
            # speed is tied
            else:
                return randint(0, 1)

    def start(self, player, enemy):
        printCentered("FIGHT", "#")
        sleep(1)

        turnOffset = self.findFirstAttacker(player, enemy)

        while True:
            if (self.turn + turnOffset) % 2 == 1:
                print("%s: %s hp\n%s: %s hp" % (enemy.name, enemy.health, player.name, player.health))
                printCentered("*press 'f' to attack or 'r' to run.*")
                move = pyip.inputMenu(["f", "r"], prompt=">")
                if move == "f":
                    rawDamage = player.attack(enemy, self.sneakAttack == player)
                    print("%s hits %s and deals %s damage!" % (player.name, enemy.name, rawDamage))
                    printLine("-")
                    sleep(1)
                    if enemy.health <= 0:
                        print(enemy.name + " was defeated!\n")
                        printLine("#")
                        print("loot %s? " % enemy.name)
                        if pyip.inputYesNo(">") == "yes":
                            player.loot(enemy)
                        del enemy

                        printLine("-")
                        break
                elif move == "r":
                    # if you are faster and/or are lucky you can escape battle
                    if player.speed + randint(0, 2) >= enemy.speed:
                        print("you run away safely")
                        printLine("-")
                        enemy.detected = False
                        break
                    else:
                        print("you couldn't get away!")
            else:
                rawDamage = enemy.attack(player, self.sneakAttack == enemy)
                print("%s strikes you and deals %s damage!" % (enemy.name, rawDamage))
                printLine("-")
                sleep(1)
                if player.health <= 0:
                    print("You died!")
                    exit()
            if self.sneakAttack:
                print("A Critical Hit!")
                self.sneakAttack = None
            self.turn += 1
        player.hunger -= self.turn
        player.detected = False
