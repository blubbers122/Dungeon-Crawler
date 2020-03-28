import DungeonCrawlerData as dcd
import DungeonCrawlerClasses as dcc
import pyinputplus as pyip
import shelve
import time
import textwrap
import random
# TODO: create random event bank


'''
for key, value in dcc.treasureBank.items():  # initializes treasure
    treasure = dcc.Treasure(key, value["value"], value["description"])
    treasure.addToInventory()

for key, value in dcc.weaponBank.items():  # initializes weapons
    weapon = dcc.Weapon(key, value["value"], value["damageMult"], value["description"])
    weapon.addToInventory()

for key, value in dcc.armorBank.items():  # initializes armor
    armor = dcc.Armor(key, value["value"], value["resistanceMult"], value["description"])
    armor.addToInventory()
'''

# TODO: define classes for all possible gameObjects (Person, Room, Item, Menu)

# TODO: define console box width, (and height?)

# TODO: check for save file in directory with valid save data

    # TODO: if empty, display New Game title screen
def newGameScreen():
    consoleWidth = 115
    difficulty = "medium"
    while True:
        line = "=" * consoleWidth
        print(line)
        if consoleWidth == 115:
            print(dcd.bigTitle.center(consoleWidth))
        else:
            print(dcd.smallTitle.center(consoleWidth))
        print("A text-based Dungeon Simulator made by blubbers122\n".center(consoleWidth))
        print("Press 'o' for options or enter to begin.".center(consoleWidth))
        print(line)
        if input() != "o":
            break
        else:
            newSettings = displayOptions(consoleWidth, difficulty)
            consoleWidth = newSettings[0]
            difficulty = newSettings[1]
    createChar(consoleWidth)


def displayOptions(consoleWidth, difficulty):
    while True:
        optionsDisplay = "Options".center(consoleWidth, "-") + "\ns: change console size\nd: change difficulty\nc: view game hotkeys\nb: return to menu\n" + "-" * consoleWidth + "\n"
        difficultyDisplay = "Change Difficulty".center(consoleWidth, "-") + "\nEasy\nMedium\nHard\n" + "-" * consoleWidth + "\n"
        controlsDisplay = "In-Game Controls".center(consoleWidth, "-")
        choice = pyip.inputMenu(["s", "d", "c", "b"], prompt=optionsDisplay)
        if choice == "s":
            consoleWidth = 187 - consoleWidth
            print("console size updated.")
        elif choice == "d":
            difficulty = pyip.inputMenu(["easy", "medium", "hard"], prompt=difficultyDisplay)
            print("difficulty was updated to " + difficulty)
        elif choice == "c":
            print(controlsDisplay)
            print("i: display inventory\nc: display in-game commands\ns: see character status\ne: end current turn\nq: exit game")
            time.sleep(2)
        else:
            break
    return consoleWidth, difficulty


def createChar(consoleWidth):
    maxPoints = 20
    while True:
        print("Create your Character".center(consoleWidth, "-"))
        name = pyip.inputStr(">What is your name? ")
        for line in textwrap.wrap("You have up to %s skill points to spend however you like on your starting health, strength and speed." % maxPoints, width=consoleWidth):
            print(line.center(consoleWidth))
        print()
        health = pyip.inputInt(">Enter health: ", min=1, max=maxPoints - 2)
        print(("Points remaining: " + str(maxPoints - health)).center(consoleWidth))
        strength = pyip.inputInt(">Enter strength: ", min=1, max=maxPoints - 1 - health)
        print(("Points remaining: " + str(maxPoints - health - strength)).center(consoleWidth))
        speed = pyip.inputInt(">Enter speed: ", min=1, max=maxPoints - health - strength)
        print(("Points remaining: " + str(maxPoints - health - strength - speed)).center(consoleWidth))
        time.sleep(.5)
        confirm = pyip.inputYesNo("%s will have %s health, %s strength and %s speed.\n>Is this okay? "
                                  % (name, health, strength, speed))
        print(speed)
        if confirm == "yes":
            player = dcc.Player(name, health, strength, 0, speed)
            print("Entering the dungeon", end="")
            for x in range(3):
                print(".", end="")
                time.sleep(.5)
            print()
            break
    dungeon(consoleWidth, player)




    # TODO: if data can be read from save file, display Continue title screen

# TODO: character selection menu

# TODO: enter dungeon and generate
def dungeon(consoleWidth, player):
    print("****To display in game commands press 'c'****".center(consoleWidth))
    time.sleep(1)
    print("IN THE DUNGEON".center(consoleWidth, "="))
    playing = True
    turn = 1
    for line in textwrap.wrap(player.name + " enters the dark cave hidden in the side of a great mountain, after hearing of a great treasure located deep inside. Despite the infamy of the dungeon, " + player.name + " trudges into the darkness.", width=consoleWidth):
        print(line.center(consoleWidth))
    while playing:
        print(("Turn %s" % turn).center(consoleWidth, "~"))
        while True:  # loops until turn ends
            nextMove = pyip.inputStr(">")
            if nextMove == "i":  # display inventory
                print("Inventory".center(consoleWidth, "-"))
                print("enter the id of the item to inspect or press 0 to go back:".center(consoleWidth))
                player.displayInventory()
                print("-" * consoleWidth)
            elif nextMove == "c":  # display commands
                showCommands(consoleWidth)
            elif nextMove == "s":  # display character status
                print(player.name.center(consoleWidth, "-"))
                player.status()
                print("Equipment".center(consoleWidth, "-"))
                player.equipment()
                print("-" * consoleWidth)
            elif nextMove == "e":  #end current turn
                break
            elif nextMove == "q":
                if pyip.inputYesNo(">Would you like to save and quit game? ") == "yes":
                    exit()
        player.hunger -= 1
        print(player.hunger)
        turn += 1


def showCommands(consoleWidth):
    print("In-Game Controls".center(consoleWidth, "-"))
    print("i: display inventory\nc: display in-game commands\ns: see character status\ne: end current turn\nq: save and quit")
    print("-" * consoleWidth)
    # TODO: check for spawning enemy

# TODO: combat

# TODO: looting

# TODO: inventory menu
    # TODO: inspect items

# TODO: levels in dungeon

# TODO:

newGameScreen()