from ..items import Item

weaponBank = {
    # "fists": {"value": 0,
    #           "damageMult": 1},
    "iron sword": {"value": 16,
                   "damageMult": 1.5,
                   "description": "An iron longsword, with a slightly rusted blade."},
    "metal lance": {"value": 22,
                    "damageMult": 1.6,
                    "description": "This is heavy, who knows if I can use it effectively."},
    "iron dagger": {"value": 9,
                   "damageMult": 1.2,
                   "description": "Well, it's a little better than a butter knife I guess..."},
    "short bow": {"value": 27,
                   "damageMult": 1.8,
                   "description": "A quick bow."},
}

class Weapon(Item):
    def __init__(self, name=None, amount=None):
        super().__init__(name, amount)
        self.value = weaponBank[self.name]["value"]
        self.description = weaponBank[self.name]["description"]
        self.damageMult = weaponBank[self.name]["damageMult"]

    types = list(weaponBank.keys())

    maxFindableStack = 1

    equippable = True
