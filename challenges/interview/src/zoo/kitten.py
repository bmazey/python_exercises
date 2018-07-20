from challenges.interview.src.zoo.mammal import Mammal


class Kitten(Mammal):
    """this is our Kitten class which 'extends' Mammal"""
    # TODO - implement this class!
    def __init__(self, name):
        self.name = name
        self.warm_blooded = True
        self.vertebrate = True
        self.size = 1
        self.legs = 4
        self.color = 'Orange'


    # examples ... using @property later
    def is_warm_blooded(self):
        return self.warm_blooded

    def is_vertebrate(self):
        return self.vertebrate

    def call(self):
        return 'meow ... meow ...'

    # all mammals have specialized teeth ... they eat differently!
    # @override
    def eat(self):
        return 'munch ... munch ...'
