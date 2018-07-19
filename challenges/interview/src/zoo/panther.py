from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""
    # TODO - implement this class!
    def __init__(self, name):
        super().__init__(name)
        self.size = 5
        self.color = 'black'

    def color(self):
        return self.color

    def get_size(self):
        return self.size

    def call(self):
        return 'ROAR!'

