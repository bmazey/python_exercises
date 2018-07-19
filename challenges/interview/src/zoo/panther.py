from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""
    size = 5
    legs = 4
    color = 'black'

    def __init__(self, name):
        super().__init__(name)

    def call(self):
        return "ROAR!"
