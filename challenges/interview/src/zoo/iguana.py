from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
    """this is our public Iguana class, which 'extends' Reptile"""
    # TODO - implement this class!
    def __init__(self,name):
        super().__init__(name)
        self.size = 3
        self.legs = 4
        self.color = 'green'

    def eat(self):
        return 'crunch ... crunch ...'
