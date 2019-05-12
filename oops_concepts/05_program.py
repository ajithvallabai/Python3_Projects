class Fruit:
    origin="asia"
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("I am eating {} fruit".format(self.name))
    def setTaste(self,taste):
        self.taste=taste
    def getTaste(self):
        return self.taste

fruitOne=Fruit("Lemon")
fruitOne.setTaste("sour")
print(fruitOne.getTaste())
