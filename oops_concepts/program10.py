# Multiple Inheritance
class Fish:
    def swim(self):
        return "I swim in water"
class Squirrel:
    def climb(self):
        return "I run in land"

class Tortoise(Fish,Squirrel):
    pass

Animal=Tortoise()

print(Animal.swim())
print(Animal.climb())

# class Fish:
#     def swim():
#         return "I swim in water"
# class Squirrel:
#     def climb(self):
#         return "I run in land"

# class Tortoise(Fish,Squirrel):
#     pass

# Animal=Tortoise()
# print(Tortoise.swim())
# print(Animal.swim())
# print(Animal.climb())