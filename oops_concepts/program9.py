# inheritance principle 
class Cat(object):
    def __init__(self,name):
        self.name=name

    def shout(self):
        print("Miaow")
    def run(self):
        print("Running")
    def sleep(self):
        print("Sleep")

AnimalOne=Cat("kitten")


# Class Cat is inherited by tiger
class Tiger(Cat):
    def shout(self):
        print("Waraawwww!! Wrawwww!!")
AnimalTwo=Tiger("Tom")


# check whether animal 2 has characterisitcs of animal 1 
class Fruit():
    def taste(self):
        print("sour")
# check tiger is a subclass of cat
print(issubclass(Tiger,Cat))

# check Tiger is a subclass of fruit
print(issubclass(Tiger,Fruit))

# check Cat is a subclass of Tiger
print(issubclass(Cat,Tiger))

# Isinstance 
# check whether AnimalOne is a object/instance of Cat
print(isinstance(AnimalOne,Cat))


