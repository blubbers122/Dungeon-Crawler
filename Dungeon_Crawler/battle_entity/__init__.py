class Entity:
    def __init__(self, name, strength, speed):
        self.name = name
        self.strength = strength
        self.speed = speed

    def attack(self):
        print(self.name + " hits their opponent.")

    def person(self):
        print("I am person")
