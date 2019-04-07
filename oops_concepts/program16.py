# inheritance 

class Human:
    def __init__(self,ability1,ability2):
        self.ability1=ability1
        self.ability2=ability2

class Lion:
    def __init__(self,ability3,ability4):
        self.ability3=ability3
        self.ability4=ability4

class KingOfJungle(Human,Lion):
    def __init__(self,ability1,ability2,ability3,ability4,ability5):
        self.ability5=ability5
        Human.__init__(self,ability1,ability2)
        Lion.__init__(self,ability3,ability4)



Zathura=KingOfJungle("breathe","run","roar","fight","courage")
print(Zathura.ability4)