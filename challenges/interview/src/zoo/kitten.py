from challenges.interview.src.zoo.mammal import Mammal


class Kitten(Mammal):
    """this is our Kitten class which 'extends' Mammal"""
    size = 1
    legs = 4
    color = 'orange'

    def __init__(self, name):
        super().__init__(name)

    def call(self):
        return "meow ... meow ..."
