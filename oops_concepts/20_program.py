
def world(word):
    def avatar(word):
        return word+" Krishna "
    return avatar

@world
def hare(word):
    return word

print(hare("Hare"))