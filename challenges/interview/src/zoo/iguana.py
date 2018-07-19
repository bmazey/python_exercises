from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
    """this is our public Iguana class, which 'extends' Reptile"""
    size = 3
    legs = 4
    color = 'green'

    def __init__(self, name):
        super().__init__(name)

    # @override
    def eat(self):
        return "crunch ... crunch ..."

    def get_color(self):
        return color