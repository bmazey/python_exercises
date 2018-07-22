from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
    """this is our public Iguana class, which 'extends' Reptile"""
    # TODO - implement this class!

    # initializes iguana object
    def __init__(self, name):
        super().__init__(name)
        super().is_warm_blooded()
        super().is_vertebrate()
        self.size = 3
        self.legs = 4
        self.color = 'green'

    # how an iguana eats
    def eat(self):
        return "crunch ... crunch ..."

    # method to get color of iguana
    def get_color(self):
        return self.color

    # method to get size of iguana
    def get_size(self):
        return self.size

    # method to get number of legs of an iguana
    def get_legs(self):
        return self.legs
