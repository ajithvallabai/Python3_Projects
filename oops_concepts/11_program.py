# Multiple Inheritance
class Fish:
    def __init__(self):
        self.ability1="swim"
        print("Base 1")
class Squirrel:
    def __init__(self):
        self.ability2="run"
        print("Base 2")

class Tortoise(Fish,Squirrel):
    def __init__(self):
        Fish.__init__(self)
        Squirrel.__init__(self)
        print("Derived")
    def inheritedAbility(self):
        print("I am Tortoise i can "+self.ability1+" and "+self.ability2)

Animal=Tortoise()
Animal.inheritedAbility()