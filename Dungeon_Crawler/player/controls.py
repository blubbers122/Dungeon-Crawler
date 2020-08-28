from ..display import printMenu, printCentered, printLine
import pyinputplus as pyip
from time import sleep

def showPlayerInventory(player):
    # the indices corresponding to the items that can be chosen in inventory

    while True:
        validChoices = [str(x) for x in range(1, len(player.inventory) + 1)]
        validChoices.append("b")
        inventory = player.inventoryStrings()
        printMenu(inventory, topText="Inventory")
        printCentered("*enter the number to inspect or press 'b' to return*")
        choice = pyip.inputChoice(validChoices, prompt=">")
        if choice == "b":
            printLine("-")
            break
        item = player.inventory[int(choice) - 1]
        printMenu(item.itemStrings(), topText=item.name)
        if item.equippable:
            printCentered("*press 'e' to equip, 'd' to drop, or 'b' to return*")
            choice = pyip.inputChoice(["e", "d", "b"], prompt=">")
            if choice == "e":
                player.equip(item)
            elif choice == "d":
                player.dropItem(item)
        elif item.usable:
            printCentered("*press 'e' to use, 'd' to drop, or 'b' to return*")
            choice = pyip.inputChoice(["e", "d", "b"], prompt=">")
            if choice == "e":
                player.consumeItem(item)
            elif choice == "d":
                player.dropItem(item)
        else:
            printCentered("*press 'd' to drop or 'b' to return*")
            choice = pyip.inputChoice(["e","d", "b"], prompt=">")
            if choice == "d":
                player.dropItem(item)


def showControls(player):
    printMenu(["i: display inventory", "c: display in-game commands", "s: see character status", "e: end current turn", "m: view map", "l: look around", "q: save and quit"],
        topText="In-Game Controls",
        bottom=True)

def showPlayerStatus(player):
    printMenu(player.status(), topText=player.name)
    printMenu(player.equipment(), topText="Equipped", bottom=True)
    sleep(1)

# TODO: a few numbers inputs to choose options when encountering a random event

# TODO: r for running away from enemies (success based on speed)
def runAway(player):
    pass

# TODO: f for engage in fight after spotting enemy
def fight(player):
    pass

def quitGame(player):
    if pyip.inputYesNo(">Would you like to save and quit game? ") == "yes":
        print("Thanks for playing!")
        exit()
    else:
        printLine("-")

# TODO: l for look around that describes current room closely but uses turn and makes you vulnerable
def lookAround(player):
    print("%s looks around." % player.name)

def endTurn(player):
    print("%s continues through %s." % (player.name, player.currentRoom.name))
    player.roomLocation += 1

def map(player):
    print(player.currentRoom)
