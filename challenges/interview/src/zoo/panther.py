from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""
    # TODO - implement this class!
    def __init__(self, name):
        super().__init__(name)
        self.size = 5
        self.legs = 4
        self.color = 'black'

    def call(self):
        return "ROAR!"

    def color(self):
        return self.color

    def is_warm_blooded(self):
        return self.is_warm_blooded

    def is_vertebrate(self):
        return self.is_vertebrate
