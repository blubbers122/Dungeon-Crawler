import pyinputplus as pyip
import time
from textwrap import wrap
from random import randint
from .events import eventBank
from .settings import difficulty
from .enemies.classes import Bat
from .display import *
from.combat import Combat

# TODO: display combat menu if you press 'm?' on turn to heal and use special items
# TODO: make it harder to run away if you are slower


# TODO: decide if spawn enemy, if they spot you or you spot them
def turnGenerator():
    roll = randint(0, len(eventBank) - 1)
    return eventBank[roll]


# TODO: add special event related functions to call if you roll for them in turnGenerator
def gamePlayLoop(player):
    playing = True
    turn = 1
    while playing:
        printCentered("Turn %s" % turn, "~")
        eventRoll = randint(0, 100)
        if eventRoll > 80:
            event = turnGenerator()
            print(event)
        if turn == 2:
            enemy = Bat()  # temporary to test combat
            print(enemy.name + " approaches")
            Combat(player, enemy)
        while True:
            nextMove = pyip.inputMenu(["c", "i", "e", "q", "s", "f", "l", "r"], ">")
            if nextMove == "e":
                break
            player.moveSet[nextMove](player)  # calls function associated with command

        player.hunger -= 1
        turn += 1


def enterDungeon(player):
    print(str(player.name) + " enters the dungeon", end="")
    for x in range(3):
        print(".", end="")
        time.sleep(.5)
    print()
    printCentered("****To display in game commands press 'c'****", " ")
    time.sleep(1)
    printCentered("IN THE DUNGEON", "=")

    printWrapped("%s enters the dark cave hidden in the side of a great mountain, after hearing of a great treasure located deep inside. Despite the infamy of the dungeon, %s trudges into the darkness." % (player.name, player.name))
    gamePlayLoop(player)


    # TODO: check for spawning enemy

# TODO: combat

# TODO: generate rooms and enemies and loot containers

# TODO: looting

# TODO: levels in dungeon
