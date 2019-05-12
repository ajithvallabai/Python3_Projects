# proper inheritance method
class Base(object): 
    def __init__(self, a): 
        self.number = a 
    def doubleup(self): 
        self.number *= 2
  
class Derived(Base):  ### you have to mention base class <------
    def __init__(self, a): 
        Base.__init__(self, a)  ### only if you declare this you can use parent class variables as "self" or as dervied class itslef <---
    def tripleup(self): 
        self.number *= 3
  
objectOne = Derived(4) 
print(objectOne.number) 
  
objectOne.doubleup() 
print(objectOne.number) 
  
objectOne.tripleup() 
print(objectOne.number) 