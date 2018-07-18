from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""
    # TODO - implement this class!

    def __init__(self, name):
        super().__init__(name)
        self.size = 5
        self.leg = 4
        self.color = "black"

    # all mammals have specialized teeth ... they eat differently!
    # @override
    def eat(self):
        return 'munch ... munch ...'

    def call(self):
        return "ROAR!"

print(Panther("hhh").eat())
