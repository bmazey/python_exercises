from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
    """this is our public Iguana class, which 'extends' Reptile"""

    # TODO - implement this class!
    def __init__(self, name):
        self.name = name
        self.warm_blooded = False
        self.vertebrate = True
        self.size = 3
        self.legs = 4
        self.color = 'green'

    # examples ... using @property later
    def is_warm_blooded(self):
        return self.warm_blooded

    def is_vertebrate(self):
        return self.vertebrate

    def get_size(self):
        return self.size

    def get_legs(self):
        return self.legs

    def get_color(self):
        return self.color

    # all mammals have specialized teeth ... they eat differently!
    # @override
    def eat(self):
        return 'crunch ... crunch ...'
