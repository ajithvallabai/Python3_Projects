"""
__init__ method
"""



class Fruit:
    def __init__(self,name):
        self.name=name 
    def eating(self):
        print("I am eating {}".format(self.name))
fruitOne=Fruit("Orange")
fruitOne.eating()