import pyinputplus as pyip
from time import sleep
from .player.classes import Warrior, Ranger, Rogue, Deprived
from .DungeonCrawler import enterDungeon
from .display import printLine, printCentered, printTitleScreen, printWrapped, printMenu

import sys
sys.path.append("C:/Users/Brock/Documents/GitHub/Dungeon-Crawler/Dungeon_Crawler")
import settings

classNames = ["Warrior", "Ranger", "Rogue", "Deprived (No starting gear)"]

presetChars = [Warrior(7, 5, "Warrior"), Ranger(6, 7, "Ranger"), Rogue(5, 9, "Rogue"), Deprived(3, 3, "Deprived")]


def play():
    newGameScreen()

def newGameScreen():
    difficulty = "medium"
    while True:
        printTitleScreen()
        if input() != "o":
            break
        else:
            difficulty = displayOptions(difficulty)
    if pyip.inputYesNo(">Create your own character? ") == "yes":
        createChar()
    else:
        chooseChar()


def displayOptions(difficulty):
    while True:
        printMenu(["s: change console size", "d: change difficulty", "c: view game hotkeys", "b: return to menu"],
            topText="Options")
        choice = pyip.inputMenu(["s", "d", "c", "b"], prompt=">")
        if choice == "s":
            settings.consoleWidth = 187 - settings.consoleWidth
            print("console size updated.")
        elif choice == "d":
            printMenu(["Easy","Normal", "Hard"], topText="Change Difficulty")
            difficulty = pyip.inputMenu(["easy", "normal", "hard"], prompt=">")
            printLine("-")
            print("difficulty was updated to " + difficulty)
        elif choice == "c":
            printMenu(["i: display inventory", "c: display in-game commands", "s: see character status", "e: end current turn", "q: quit game"], topText="In-Game Controls")
            sleep(1)
        else:
            break
    return difficulty


def chooseChar():
    while True:
        printMenu(["%s: %s" % (index + 1, className) for index, className in enumerate(classNames)],
            topText="Choose your Character")
        choice = pyip.inputInt(">", min=1, max=4)
        player = presetChars[choice - 1]
        enterDungeon(player)

def createChar():
    maxPoints = 20
    while True:
        printMenu(["What is your name?"], topText="Create your Character")
        name = pyip.inputStr(">")

        printMenu(["%s: %s" % (count + 1, className) for count, className in enumerate(classNames)])
        print("Choose your class: ")
        playerClass = pyip.inputInt(">", min=1, max=len(classNames))
        print("You chose %s" % classNames[playerClass - 1])

        if playerClass == 4:
            maxPoints /= 2

        printLine("-")
        printWrapped("You have up to %s skill points to spend however you like on your starting health, strength and speed." % maxPoints)

        # add for loop here
        strength = pyip.inputInt(">Enter strength: ", min=1, max=maxPoints - 1)
        printLine("-")
        printCentered("Points remaining: " + str(maxPoints - strength))
        speed = pyip.inputInt(">Enter speed: ", min=1, max=maxPoints - strength)
        printLine("-")
        printCentered("Points remaining: " + str(maxPoints - strength - speed))
        sleep(.5)
        confirm = pyip.inputYesNo("%s will have %s strength and %s speed.\n>Is this okay? "
                                  % (name, strength, speed))

        # replace with dictionary
        if confirm == "yes":
            if playerClass == 1:
                player = Warrior(name, strength, speed)
            elif playerClass == 2:
                player = Ranger(name, strength, speed)
            elif playerClass == 3:
                player = Rogue(name, strength, speed)
            else:
                # change to allow Deprived
                player = Deprived(name, strength, speed)
                pass
            break
    enterDungeon(player)
