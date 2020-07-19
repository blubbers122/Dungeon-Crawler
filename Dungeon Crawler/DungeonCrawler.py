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

defaultInventory = {
    "gold coin": 50,
}

classes = ["Warrior", "Ranger", "Rogue", "Deprived (No starting gear)"]

presetChars = [dcc.Warrior("Warrior", 7, 5, defaultInventory), dcc.Ranger("Ranger", 6, 7, defaultInventory), dcc.Rogue("Rogue", 5, 9, defaultInventory), dcc.Player("Deprived", 3, 3, {})]

enemies = []

eventBank = ["enemy spotted", "enemy sneaks up on you", "you trip on something",
             "loose rock blocks path", "loose rock hits you", "you wake up sleeping enemy",
             "stumble open hidden item/chest", "item was cursed", "trapped chest",
             "enemy poisons you", "something shiny sticking out of rubble", "branching path",
             "hear a noise", "smell something"]

# TODO: check for save file in directory with valid save data

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
    if pyip.inputYesNo("Create your own character? ") == "yes":
        createChar(consoleWidth)
    else:
        chooseChar(consoleWidth)


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
            print("i: display inventory\nc: display in-game commands\ns: see character status\ne: end current turn\nq: quit game")
            time.sleep(2)
        else:
            break
    return consoleWidth, difficulty


def chooseChar(consoleWidth):
    while True:
        print("Choose your Character".center(consoleWidth, "-"))
        for index, classname in enumerate(classes):
            print("%s: %s" % (index + 1, classname))
        choice = pyip.inputInt(">", min=1, max=4)
        player = presetChars[choice - 1]
        dungeon(consoleWidth, player)



def createChar(consoleWidth):
    maxPoints = 20
    while True:
        print("Create your Character".center(consoleWidth, "-"))
        name = pyip.inputStr(">What is your name? ")
        for count, classname in enumerate(classes):
            print("%s: %s" % (count + 1, classname))
        playerClass = pyip.inputInt(">Choose your class ", min=1, max=len(classes))
        if playerClass == 4:
            maxPoints /= 2
        for line in textwrap.wrap("You have up to %s skill points to spend however you like on your starting health, strength and speed." % maxPoints, width=consoleWidth):
            print(line.center(consoleWidth))
        print()
        #health = pyip.inputInt(">Enter health: ", min=1, max=maxPoints - 2)
        #print(("Points remaining: " + str(maxPoints - health)).center(consoleWidth))
        strength = pyip.inputInt(">Enter strength: ", min=1, max=maxPoints - 1)
        print(("Points remaining: " + str(maxPoints - strength)).center(consoleWidth))
        speed = pyip.inputInt(">Enter speed: ", min=1, max=maxPoints - strength)
        print(("Points remaining: " + str(maxPoints - strength - speed)).center(consoleWidth))
        time.sleep(.5)
        confirm = pyip.inputYesNo("%s will have %s strength and %s speed.\n>Is this okay? "
                                  % (name, strength, speed))
        if confirm == "yes":
            if playerClass == 1:
                player = dcc.Warrior(name, strength, speed, defaultInventory)
            elif playerClass == 2:
                player = dcc.Ranger(name, strength, speed, defaultInventory)
            elif playerClass == 3:
                player = dcc.Rogue(name, strength, speed, defaultInventory)
            else:
                player = dcc.Player(name, strength, speed, {})
            break
    dungeon(consoleWidth, player)

    # TODO: if data can be read from save file, display Continue title screen

# TODO: character selection menu

# TODO: enter dungeon and generate

def i(consoleWidth, player):
    print("Inventory".center(consoleWidth, "-"))
    print("enter the name of the item to inspect or press b to go back:".center(consoleWidth))
    player.displayInventory()
    print("-" * consoleWidth)

def c(consoleWidth, player):
    print("In-Game Controls".center(consoleWidth, "-"))
    print(
        "i: display inventory\nc: display in-game commands\ns: see character status\ne: end current turn\nq: save and quit")
    print("-" * consoleWidth)

def s(consoleWidth, player):
    print(player.name.center(consoleWidth, "-"))
    player.status()
    print("Equipment".center(consoleWidth, "-"))
    player.equipment()
    print("-" * consoleWidth)

# TODO: a few numbers inputs to choose options when encountering a random event

# TODO: r for running away from enemies (success based on speed)
def r(consoleWidth, player):
    pass

# TODO: f for engage in fight after spotting enemy
def f(consoleWidth, player):
    # enemySpotted and enemyExists
    if enemies != []:
        print("You approach enemy " + enemies[0].name)
        combat(consoleWidth, player, enemies[0])
    else:
        print("you cannot fight now.")

def q(consoleWidth, player):
    if pyip.inputYesNo(">Would you like to save and quit game? ") == "yes":
        exit()

# TODO: l for look around that describes current room closely but uses turn and makes you vulnerable
def l(consoleWidth, player):
    pass

moveSet = {
    "i": i,
    "c": c,
    "s": s,
    "r": r,
    "f": f,
    "q": q,
    "l": l
}


# TODO: display combat menu if you press 'm?' on turn to heal and use special items
# TODO: make it harder to run away if you are slower
def combat(consoleWidth, player, enemy):
    print("FIGHT".center(consoleWidth, "#"))
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
                rawDamage = player.strength * player.damageMult - enemy.defense + random.randint(-2, 2)
                if rawDamage <= 0:
                    rawDamage = 1
                enemy.health -= rawDamage
                print("%s hits %s with %s and deals %s damage!\n" % (player.name, enemy.name, player.weapon, rawDamage))
                time.sleep(1)
                if enemy.health <= 0:
                    print(enemy.name + " was defeated!\n")
                    # TODO: add looting here
                    if pyip.inputYesNo(">loot %s? " % enemy.name) == "yes":
                        print(enemy.name.center(consoleWidth, "-"))
                        enemy.displayInventory()
                        print("-" * consoleWidth)
                    break
            else:
                print("you run away")
                break
        else:
            rawDamage = enemy.strength - player.defense + random.randint(-2, 2)
            if rawDamage <= 0:
                rawDamage = 1
            player.health -= rawDamage
            print("%s strikes you and deals %s damage!\n" % (enemy.name, rawDamage))
            time.sleep(1)
            if player.health <= 0:
                print("You died!")
                exit()
        count += 1
    del enemies[0]
    player.hunger -= count
    print("#" * consoleWidth)

# TODO: decide if spawn enemy, if they spot you or you spot them
def turnGenerator():
    roll = random.randint(0, len(eventBank) - 1)
    return eventBank[roll]


# TODO: add special event related functions to call if you roll for them in turnGenerator

def dungeon(consoleWidth, player):
    print(player.name + " enters the dungeon", end="")
    for x in range(3):
        print(".", end="")
        time.sleep(.5)
    print()
    print("****To display in game commands press 'c'****".center(consoleWidth))
    time.sleep(1)
    print("IN THE DUNGEON".center(consoleWidth, "="))
    playing = True
    turn = 1
    for line in textwrap.wrap(player.name + " enters the dark cave hidden in the side of a great mountain, after hearing of a great treasure located deep inside. Despite the infamy of the dungeon, " + player.name + " trudges into the darkness.", width=consoleWidth):
        print(line.center(consoleWidth))
    while playing:
        print(("Turn %s" % turn).center(consoleWidth, "~"))
        event = turnGenerator()
        print(event)
        if turn == 2:
            enemies.append(dcc.Bat())  # temporary to test combat
        if enemies != [] and random.randint(1, 5) == 5:
            print(enemies[0].name + " approaches")
            combat(consoleWidth, player, enemies[0])
        while True:  # loops until turn ends
            nextMove = pyip.inputMenu(["c", "i", "e", "q", "s", "f", "l", "r"], ">")
            if nextMove == "e":
                break
            moveSet[nextMove](consoleWidth, player)  # calls function associated with command
        player.hunger -= 1
        turn += 1

    # TODO: check for spawning enemy

# TODO: combat

# TODO: generate rooms and enemies and loot containers

# TODO: looting

# TODO: levels in dungeon

# TODO:

newGameScreen()