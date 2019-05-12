# Modifying Parent class name 

class Cat:
    def __init__(self,ablity1):
        self.ablity1=ablity1
        self.ablity3="watch"
class Tiger(Cat):
    def __init__(self,ablity1,ablity2):
        super(Tiger,self).__init__(ablity1)
        
        self.ablity2=ablity2
    
#animalOne=Cat("run at 20km/hr")
animalTwo=Tiger("run at 40km/hr","breathe")
print("I am a tiger i can "+animalTwo.ablity1+" and "+animalTwo.ablity2)
print("I am a tiger i can "+animalTwo.ablity3+" and "+animalTwo.ablity2)

animalOne=Cat()



