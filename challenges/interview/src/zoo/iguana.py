from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
    """this is our public Iguana class, which 'extends' Reptile"""
    # TODO - implement this class!
    def __int__(self, name):
        super().__int__(name)


    def get_size(self):
        return 3


    def get_legs(self):
        return 4


    def get_color(self):
        return 'green'


    def eat(self):
        return "crunch ... crunch ..."
