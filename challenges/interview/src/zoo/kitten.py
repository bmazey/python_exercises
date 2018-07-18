from challenges.interview.src.zoo.mammal import Mammal


class Kitten(Mammal):
    """this is our Kitten class which 'extends' Mammal"""
    # TODO - implement this class!
    def __init__(self,name):
        super().__init__(name)
        self.size = 1
        self.legs = 4
        self.color = 'orange'

    def call(self):
        return 'meow ... meow ...'