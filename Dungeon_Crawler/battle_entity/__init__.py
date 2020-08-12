class Entity:
    def __init__(self, strength, speed):
        self.strength = strength
        self.speed = speed

    def attack(self):
        print(self.name + " hits their opponent.")

    def defend(self):
        pass

    
