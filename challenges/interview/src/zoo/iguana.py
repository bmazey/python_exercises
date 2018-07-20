from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
    """this is our public Iguana class, which 'extends' Reptile"""
    # TODO - implement this class!
    def __init__(self, name):
        self.name = name
        self.color = 'green'
        self.warm_blooded = False
        # all Animals eat

    def eat(self):
        return "crunch ... crunch ..."

    def is_warm_blooded(self):
        return self.warm_blooded

    def get_color(self):
        return self.color

    def get_size(self):
        return 3

    def get_legs(self):
        return 4



