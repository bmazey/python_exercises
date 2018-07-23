from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.legs = 4
        self.size = 5
        self.color = 'black'
        # self.eat = 'munch ... munch ...'
        # self.call = 'ROAR!'

    def call(self):
        return "ROAR!"






