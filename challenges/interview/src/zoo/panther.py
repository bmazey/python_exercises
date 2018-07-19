from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""
    # TODO - implement this class!
    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = True
        self.vertebrate = True
        self.size = 5
        self.legs = 4
        panther.color = "black"


    # examples ... using @property later
    def is_warm_blooded(self):
        return self.warm_blooded

    def is_vertebrate(self):
        return self.vertebrate

    # all mammals have specialized teeth ... they eat differently!
    # @override
    def eat(self):
        return 'munch ... munch ...'
    def call(self):
        return "ROAR!"