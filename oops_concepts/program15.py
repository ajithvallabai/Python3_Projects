## Accessing parent class and changing the variables 

class Animal:
    def __init__(self,ability1):
        self.ability1=ability1
        
class Lion(Animal):                         # <-------------
    def __init__(self,ability1):        
        super(Lion,self).__init__(ability1) # <--------------
    def shout(self):
        return "roar"

animalOne=Lion("run")
print(animalOne.ability1)


