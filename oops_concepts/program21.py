# *args and **kwargs 

# *args used to pass non-keyworded arguments eg: "hi","hello"
def printSomeThing1(*args):
    print(*args)

printSomeThing1("Hi ","Hello",[3,4,5],5,8.0)

# you can get the first variable with a desired word
def printSomeThing1A(word,*args):
    print(word)
    print(*args)

printSomeThing1A("Hi ","Hello",[3,4,5],5,8.0)


# **kwargs used to pass keyworded argumnets and it forms a dictionary 
# you can iter thorught he dictionary and get needed values
def printSomeThing2(**kwargs):
    print(kwargs)

printSomeThing2(one="a",two="b",three="c")

