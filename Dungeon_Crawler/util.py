from random import randint

# takes a dict of options and their corresponding probability
# rolls a number and returns the key of the winner based off of the weights given
def chooseFromProbability(optionWeights):
    adjustedWeights = {}
    roll = randint(0, 100)
    previous = 0

    itemTypes = list(optionWeights.keys())

    # adds the probabilities up to be easy to choose from a roll
    # might need to be optimized?
    for key, value in optionWeights.items():
        adjustedWeights[key] = value + previous
        previous = adjustedWeights[key]

    # checks each option if it won the roll
    for type in itemTypes:
        if roll < adjustedWeights[type]:
            return type
