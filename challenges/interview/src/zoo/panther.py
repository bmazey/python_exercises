from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""
    # TODO - implement this class!

    # initializes panther class
    def __init__(self, name):
        super().__init__(name)
        super().is_warm_blooded()
        super().is_vertebrate()
        self.size = 5
        self.legs = 4
        self.color = 'black'

    # how a panther calls
    def call(self):
        return "ROAR!"

