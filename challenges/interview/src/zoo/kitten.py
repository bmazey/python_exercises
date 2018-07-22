from challenges.interview.src.zoo.mammal import Mammal


class Kitten(Mammal):
    """this is our Kitten class which 'extends' Mammal"""
    # TODO - implement this class!

    # initializes kitten object
    def __init__(self, name):
        super().__init__(name)
        super().is_warm_blooded()
        super().is_vertebrate()
        self.size = 1
        self.legs = 4
        self.color = 'orange'

    # how a kitten calls
    def call(self):
        return "meow ... meow ..."
