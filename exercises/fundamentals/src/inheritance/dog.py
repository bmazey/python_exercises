

class Dog:

    # all dogs have a name, legs, and a size
    def __init__(self, name):
        self.name = name
        self.legs = 4
        self.size = 5

    # all dogs bark
    def bark(self):
        return "bark! ... bark! ... : " + str(self.name)
