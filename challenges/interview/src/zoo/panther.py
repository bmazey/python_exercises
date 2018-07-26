from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""
    # TODO - implement this class!
    def __int__(self, name):
        super().__int__(name)
        self.legs = 4
        self.color = 'black'

    def call(self):
        return "ROAR!"

    def size(self):
        return 5