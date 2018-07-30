from challenges.interview.src.zoo.mammal import Mammal


class Kitten(Mammal):
    """this is our Kitten class which 'extends' Mammal"""
    # TODO - implement this class!
    def __int__(self, name):
        super().__int__(name)
        self.legs = 4
        self.color = 'orange'

    def call(self):
        return "ROAR!"

    def size(self):
        return 1
