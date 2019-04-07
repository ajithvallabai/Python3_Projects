class Fruit:
    __hiddenFruit="Guava"
    __hiddenFruitnumber=3
    def __init__(self):
        pass
    def add(self,increment):
        #print(self.__hiddenFruitnumber)
        self.__hiddenFruitnumber=self.__hiddenFruitnumber+increment
        print("There are {}  {} in the basket".format(self.__hiddenFruitnumber,self.__hiddenFruit))

basket=Fruit()
basket.add(3)