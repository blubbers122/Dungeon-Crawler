

def showPlayerInventory(player):
    print("Inventory".center(consoleWidth, "-"))
    print("enter the name of the item to inspect or press b to go back:".center(consoleWidth))
    player.displayInventory()
    print("-" * consoleWidth)

def showControls(player):
    print("In-Game Controls".center(consoleWidth, "-"))
    print(
        "i: display inventory\nc: display in-game commands\ns: see character status\ne: end current turn\nq: save and quit")
    print("-" * consoleWidth)

def showPlayerStatus(player):
    print(player.name.center(consoleWidth, "-"))
    player.status()
    print("Equipment".center(consoleWidth, "-"))
    player.equipment()
    print("-" * consoleWidth)

# TODO: a few numbers inputs to choose options when encountering a random event

# TODO: r for running away from enemies (success based on speed)
def runAway(player):
    pass

# TODO: f for engage in fight after spotting enemy
def fight(player):
    # enemySpotted and enemyExists
    if enemies != []:
        print("You approach enemy " + enemies[0].name)
        combat(consoleWidth, player, enemies[0])
    else:
        print("you cannot fight now.")

def quitGame(player):
    if pyip.inputYesNo(">Would you like to save and quit game? ") == "yes":
        exit()

# TODO: l for look around that describes current room closely but uses turn and makes you vulnerable
def lookAround(consoleWidth, player):
    pass

def endTurn():
    pass
