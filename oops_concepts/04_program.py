
class Fruit:
    origin="asia"
    def __init__(self,name):
        self.name=name 
    def eating(self):
        print("I am eating {}".format(self.name))

fruitOne=Fruit("Orange")
fruitTwo=Fruit("Custard")
print(fruitOne.name)
print(fruitTwo.name)

print(fruitOne.origin)