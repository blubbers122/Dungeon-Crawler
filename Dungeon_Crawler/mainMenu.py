import pyinputplus as pyip
from time import sleep
from .player.classes import Warrior, Ranger, Rogue, Deprived
from .DungeonCrawler import enterDungeon
from .display import printLine, printCentered, printTitleScreen, printWrapped

import sys
sys.path.append("C:/Users/Brock/Documents/GitHub/Dungeon-Crawler/Dungeon_Crawler")
import settings

classNames = ["Warrior", "Ranger", "Rogue", "Deprived (No starting gear)"]

presetChars = [Warrior("Warrior", 7, 5), Ranger("Ranger", 6, 7), Rogue("Rogue", 5, 9), Deprived("Deprived", 3, 3)]


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
    if pyip.inputYesNo(">Create your own character? "):
        createChar()
    else:
        chooseChar()


def displayOptions(difficulty):
    while True:
        optionsDisplay = "s: change console size\nd: change difficulty\nc: view game hotkeys\nb: return to menu\n>"
        difficultyDisplay = "Easy\nNormal\nHard\n>"

        printCentered("Options", "-")
        choice = pyip.inputMenu(["s", "d", "c", "b"], prompt=optionsDisplay)
        if choice == "s":
            settings.consoleWidth = 187 - settings.consoleWidth
            print("console size updated.")
        elif choice == "d":
            printCentered("Change Difficulty", "-")
            difficulty = pyip.inputMenu(["easy", "normal", "hard"], prompt=difficultyDisplay)
            printLine("-")
            print("difficulty was updated to " + difficulty)
        elif choice == "c":
            printCentered("In-Game Controls", "-")
            print("i: display inventory\nc: display in-game commands\ns: see character status\ne: end current turn\nq: quit game")
            sleep(2)
        else:
            break
    return difficulty


def chooseChar():
    while True:
        printCentered("Choose your Character", "-")
        for index, classname in enumerate(classNames):
            print("%s: %s" % (index + 1, classname))
        choice = pyip.inputInt(">", min=1, max=4)
        player = presetChars[choice - 1]
        enterDungeon(player)

def createChar():
    maxPoints = 20
    while True:
        printCentered("Create your Character", "-")
        name = pyip.inputStr(">What is your name? ")
        for count, classname in enumerate(classNames):
            print("%s: %s" % (count + 1, classname))
        playerClass = pyip.inputInt(">Choose your class: ", min=1, max=len(classNames))
        if playerClass == 4:
            maxPoints /= 2
        printLine("-")
        printWrapped("You have up to %s skill points to spend however you like on your starting health, strength and speed." % maxPoints)

        strength = pyip.inputInt(">Enter strength: ", min=1, max=maxPoints - 1)
        printLine("-")
        printCentered("Points remaining: " + str(maxPoints - strength), " ")
        speed = pyip.inputInt(">Enter speed: ", min=1, max=maxPoints - strength)
        printLine("-")
        printCentered("Points remaining: " + str(maxPoints - strength - speed), " ")
        sleep(.5)
        confirm = pyip.inputYesNo("%s will have %s strength and %s speed.\n>Is this okay? "
                                  % (name, strength, speed))
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
