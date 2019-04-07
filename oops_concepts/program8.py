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
AnimalOne.shout()

# Class Cat is inherited by tiger
class Tiger(Cat):
    def shout(self):
        print("Waraawwww!! Wrawwww!!")
AnimalTwo=Tiger("Tom")
AnimalTwo.shout()
AnimalTwo.run()