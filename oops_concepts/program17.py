"""
overiding 
method by which using a method/function in 
we cannot ovride a private class which has a 
__ __ in its name 

"""

class Animal(object):
    def __init__(self):
        name="Zabra"
    def run(self):
        print("walking")
class Tiger(Animal):
    def __init__(self):
        name="Critic"
        self.call()
        Animal.__init__(self)
    def run(self):
        print("running")
    def call(self):
        self.run()
        Animal.run(self)
animalOne=Tiger()



