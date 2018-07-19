from challenges.interview.src.zoo.animal import Animal


class Mammal(Animal):
    """this 'abstract class' defines a Mammal"""
    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = True
        self.vertebrate = True
        self.legs = 4
        self.eatSound = 'munch ... munch ...'

    # examples ... using @property later
    def is_warm_blooded(self):
        return self.warm_blooded

    def is_vertebrate(self):
        return self.vertebrate

    def legs(self):
        return self.legs

    def eat(self):
        return self.eatSound

    def color(self):
        return self.color

    # all mammals have specialized teeth ... they eat differently!
    # @override
