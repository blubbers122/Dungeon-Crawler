import pyinputplus as pyip
import time
from textwrap import wrap
from random import randint
from .events import eventBank
from .settings import difficulty
from .display import *
from .combat import Combat
from .rooms import Room
from .floors import Floor

# TODO: decide if spawn enemy, if they spot you or you spot them
def turnGenerator():
    roll = randint(0, len(eventBank) - 1)
    return eventBank[roll]

# calculates if player found loot, implements it, and returns True if they did
def handleFindLoot(room, player):
    for container in room.containers:
        closeToChest = player.roomLocation == container.roomLocation
        foundChest = player.perception + randint(-2, 2) + container.visibility >= 10
        print(closeToChest, foundChest)
        if closeToChest and foundChest:
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
                    print("but %s saw you and attacks" % enemy.name)
                    Combat(player, enemy)
                    room.enemies.remove(enemy)
                    room.enemyCount -= 1

def nextRoom(player, floor):
    room = Room()
    player.currentRoom = room
    player.roomLocation = 0
    floor.currentRoom = room
    room.generateContainers(floor)
    room.generateEnemies(floor)
    return room

# tells important player status information
def playerUpdate():
    pass

# TODO: add special event related functions to call if you roll for them in turnGenerator
def gamePlayLoop(player):
    playing = True
    turn = 1
    print()
    printCentered("****To display in game commands press 'c'****")

    floor = Floor()

    # builds the starting room
    room = nextRoom(player, floor)

    printCentered(floor.name, "=")

    while playing:
        print(player.roomLocation)
        if player.roomLocation >= room.size:
            print("you leave %s" % room.name)
            room = nextRoom(player, floor)
            print("you entered %s" % room.name)
            print(room.entranceMessage)
        printCentered("Turn %s" % turn, "~")

        eventRoll = randint(0, 100)
        if eventRoll > 80:
            event = turnGenerator()
            #print(event)

        handleNearbyEnemies(room, player)

        handleFindLoot(room, player)

        if player.hunger < 0:
            print("you are starving.")
            player.health -= 1
        elif player.hunger < 30:
            print("you should definitely find something to eat")
        elif player.hunger < 60:
            print("you're starting to get a little peckish")

        # interface for waiting for player's next actions before ending turn
        while True:
            printCentered(floor.name, "=")
            printCentered("Location %s/%s" % (player.roomLocation, room.size))
            nextMove = pyip.inputMenu(["c", "i", "e", "q", "s", "f", "l", "r", "m"], ">")
            player.moveSet[nextMove](player)  # calls control function associated with command
            if nextMove == "e" or nextMove == "l":
                break

        if player.hunger > 0:
            player.hunger -= 10


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
