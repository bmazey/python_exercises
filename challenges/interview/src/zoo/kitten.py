from challenges.interview.src.zoo.mammal import Mammal


class Kitten(Mammal):
    """this is our Kitten class which 'extends' Mammal"""

    def __init__(self, name):
        super().__init__(name)
        self.legs = 4
        self.size = 1
        self.color = 'orange'

    def call(self):
        return 'meow ... meow ...'

