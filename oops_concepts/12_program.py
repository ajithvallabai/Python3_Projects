# Modifying Parent class name 

class Cat:
    def __init__(self,ablity1):
        self.ablity1=ablity1
class Tiger(Cat):
    def __init__(self,ablity1,ablity2):
        Cat.ablity1=ablity1
        self.ablity2=ablity2
#animalOne=Cat("run at 20km/hr")
animalTwo=Tiger("run at 40km/hr","breathe")
print("I am a tiger i can "+animalTwo.ablity1+" and "+animalTwo.ablity2)





