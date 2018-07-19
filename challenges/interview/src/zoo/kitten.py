from challenges.interview.src.zoo.mammal import Mammal


class Kitten(Mammal):

    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = True
        self.vertebrate = True
        self.size = 1
        self.legs = 4
        self.color = 'orange'

    def call(self):
        return  'meow ... meow ...'

    def is_warm_blooded(self):
        return self.warm_blooded

    def is_vertebrate(self):
        return self.vertebrate

    # all mammals have specialized teeth ... they eat differently!
    # @override
    def eat(self):
        return 'munch ... munch ...'