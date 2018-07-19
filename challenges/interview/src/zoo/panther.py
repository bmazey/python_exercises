from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""
    # TODO - implement this class!
    def _init_(self, name):
        super().init_name()
        self.size = 5
        self.legs = 4
        self.vertebrate = True
        self.warm_blooded = True
        self.color = 'black'

    def call(self):
        return 'ROAR'

    def is_vertebrate(self):
        return self.vertebrate

    def is_warm_blooded(self):
        return self.warm_blooded


