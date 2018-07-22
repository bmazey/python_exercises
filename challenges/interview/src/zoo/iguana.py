from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
    def __init__(self, name):
        super().__init__(name)
        # sets values minus mammal values

    def get_size(self):
        return 3

    def get_legs(self):
        return 4

    def get_color(self):
        return 'green'

    def eat(self):
        return 'crunch ... crunch ...'
