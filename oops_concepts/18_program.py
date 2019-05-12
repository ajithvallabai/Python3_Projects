class Ram(object):
    def say(self):
        print("Arae Krishna")
class Krishna(Ram):
    def say(self):
        print("Arae Vishnu")
        super(Krishna,self).say()
class Vishnu(Krishna):
    def say(self):
        print("Arae Ram")
        super(Vishnu,self).say()

one=Vishnu()
one.say()