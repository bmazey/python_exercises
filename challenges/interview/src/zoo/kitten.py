from challenges.interview.src.zoo.mammal import Mammal


class Kitten(Mammal):
    """this is our Kitten class which 'extends' Mammal"""
    # TODO - implement this class!
    def __init__(self, name):
        super().__init__(name)
        self.size = 1
        self.legs = 4
        self.vertebrate = True
        self.warm_blooded = True
        self.color = 'orange'

    def call(self):
        return 'meow ... meow ...'

    def is_vertebrate(self):
        return self.vertebrate

    def is_warm_blooded(self):
        return self.warm_blooded
