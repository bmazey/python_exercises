from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""
    # TODO - implement this class!
    def __init__(self, name):
        self.name = name
        self.size = 5
        self.legs = 4
        self.vertebrate = True
        self.warm_blooded = True
        self.color = 'black'

    # examples ... using @property later

    def is_warm_blooded(self):
        return self.warm_blooded

    def is_vertebrate(self):
        return self.vertebrate

    def call(self):
        return 'ROAR!'

    # all mammals have specialized teeth ... they eat differently!
    # @override
    def eat(self):
        return 'munch ... munch ...'








