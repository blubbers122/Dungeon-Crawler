from random import randint

# any game object that can act in battle
class Entity:

    #add attack type later
    def attack(self, opponent):
        rawDamage = self.strength * self.damageMult - opponent.defense + randint(-2, 2)
        if rawDamage <= 0:
            rawDamage = 1
        opponent.health -= rawDamage

        return rawDamage

    def inventoryStrings(self):
        if self.inventory:
            strings = ["%s: %s %s" % (index + 1, item.amount, item.name) for index, item in enumerate(self.inventory)]
        else:
            strings = ["nothing here."]
        return strings

    def defend(self):
        pass
