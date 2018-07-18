from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
    """this is our public Iguana class, which 'extends' Reptile"""
    # TODO - implement this class!
    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = False
        self.color = 'green'

    def is_warm_blooded(self):
        return self.warm_blooded

    def get_size(self):
        return 3

    def get_legs(self):
        return 4

    def get_color(self):
        return 'green'

