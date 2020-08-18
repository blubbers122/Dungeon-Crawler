import pyinputplus as pyip
import time
from textwrap import wrap
from random import randint
from .events import eventBank
from .settings import difficulty
from .enemies.classes import Bat
from .display import *
from .combat import Combat
from .rooms import Room
from .floors import Floor

# TODO: display combat menu if you press 'm?' on turn to heal and use special items
# TODO: make it harder to run away if you are slower


# TODO: decide if spawn enemy, if they spot you or you spot them
def turnGenerator():
    roll = randint(0, len(eventBank) - 1)
    return eventBank[roll]

# calculates if player found loot, implements it, and returns True if they did
def handleFindLoot(room, player):
    for container in room.containers:
        #TODO: optimize to factor in player and container location too
        foundChest = player.perception + randint(-2, 2) + container.visibility >= 10

        if foundChest:
            print(container.discoveryMessage)
            print("loot?")
            if pyip.inputYesNo(">") == "yes":
                player.loot(container)
                room.containers.remove(container)
            return True
    return False

def handleNearbyEnemies(room, player):
    # checks if an enemy is in the same spot as the player
    for enemy in room.enemies:
        if player.roomLocation == enemy.roomLocation:
            print(enemy.stealth)
            # check if player noticed the enemy
            if player.perception + randint(-2, 2) > enemy.stealth:
                enemy.detected = True
                print("you notice a %s nearby." % enemy.name)
            # if enemy noticed the player
            if player.stealth + randint(-2, 2) < enemy.perception:
                player.detected = True
            else:
                if enemy.detected: print("it didn't see you")
                player.detected = False

            # can choose if you want to fight the nearby enemy you see
            if enemy.detected:
                print("attack the %s?" % enemy.name)
                if pyip.inputYesNo(">") == "yes":
                    Combat(player, enemy)
                    room.enemies.remove(enemy)
                    room.enemyCount -= 1
                    return
                print("you decide to try and leave it alone.")
            # if the enemy sees you and you don't see it,
            # it may sneak attack you
            if player.detected:
                if randint(0, 10) < enemy.aggression:
                    Combat(player, enemy)
                    room.enemies.remove(enemy)
                    room.enemyCount -= 1

def nextRoom():
    pass

# TODO: add special event related functions to call if you roll for them in turnGenerator
def gamePlayLoop(player):
    playing = True
    turn = 1
    print()
    printCentered("****To display in game commands press 'c'****")

    floor = Floor()

    # builds the starting room
    room = Room()
    room.current = True
    room.generateContainers()
    room.generateEnemies()
    #print(room.containers)
    #print(room.enemies)

    printCentered(floor.name, "=")
    printCentered("Location %s" % player.roomLocation)
    print(room)

    while playing:
        if player.roomLocation >= room.size:
            nextRoom()
        printCentered("Turn %s" % turn, "~")

        eventRoll = randint(0, 100)
        if eventRoll > 80:
            event = turnGenerator()
            #print(event)

        handleNearbyEnemies(room, player)

        handleFindLoot(room, player)

        # interface for waiting for player's next actions before ending turn
        while True:
            printCentered(floor.name, "=")
            printCentered("Location %s" % player.roomLocation)
            print(room)
            nextMove = pyip.inputMenu(["c", "i", "e", "q", "s", "f", "l", "r"], ">")
            if nextMove == "e":
                player.roomLocation += 1
                break
            player.moveSet[nextMove](player)  # calls control function associated with command

        player.hunger -= 1
        turn += 1


def enterDungeon(player):
    printLine("-")
    print(str(player.name) + " enters the dungeon", end="")

    #for x in range(3):
        #print(".", end=" ")
        #time.sleep(1)
    print()
    printCentered("IN THE DUNGEON", "=")
    printWrapped("%s enters the dark cave hidden in the side of a great mountain, after hearing of a great treasure located deep inside. Despite the infamy of the dungeon, %s trudges into the darkness." % (player.name, player.name))
    gamePlayLoop(player)

# TODO: levels in dungeon
