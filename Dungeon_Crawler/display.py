import sys
sys.path.append("C:/Users/Brock/Documents/GitHub/Dungeon-Crawler/Dungeon_Crawler")
import settings
from textwrap import wrap

def printLine(char):
    print(char * settings.consoleWidth)

def printCentered(text, spacer):
    print(text.center(settings.consoleWidth, spacer))

def printMenu(border, top, bottom, content):
    pass

def printWrapped(text):
    for line in wrap(text, width=settings.consoleWidth):
        print(line, "")

bigTitle = r'''
 ______                                                        ______                           __
|_   _ `.                                                    .' ___  |                         [  |
  | | `. \ __   _   _ .--.   .--./) .---.   .--.   _ .--.   / .'   \_| _ .--.  ,--.  _   _   __ | | .---.  _ .--.
  | |  | |[  | | | [ `.-. | / /'`\;/ /__\\/ .'`\ \[ `.-. |  | |       [ `/'`\]`'_\ :[ \ [ \ [  ]| |/ /__\\[ `/'`\]
 _| |_.' / | \_/ |, | | | | \ \._//| \__.,| \__. | | | | |  \ `.___.'\ | |    // | |,\ \/\ \/ / | || \__., | |
|______.'  '.__.'_/[___||__].',__`  '.__.' '.__.' [___||__]  `.____ .'[___]   \'-;__/ \__/\__/ [___]'.__.'[___]
                           ( ( __))


'''
smallTitle = r'''
___  _    __   ____ ____ ____ __     ____ ____ ___  _  _ __   ____ ____
|  \ || \ | \|\|  _\| __\|   || \|\  | __\| . \|  \ ||| \| |  | __\| . \
| . \||_|\|  \|| [ \|  ]_| . ||  \|  | \__|  <_| . \||\ /| |__|  ]_|  <_
|___/|___/|/\_/|___/|___/|___/|/\_/  |___/|/\_/|/\_/|/\/ |___/|___/|/\_/
'''

def printTitleScreen():
    printLine("=")
    if settings.consoleWidth == 115:
        print(bigTitle)
    else:
        print(smallTitle)
    printCentered("A text-based Dungeon Simulator made by blubbers122", " ")
    printCentered("Press 'o' for options or enter to begin.", " ")
    printLine("=")
