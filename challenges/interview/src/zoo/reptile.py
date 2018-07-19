from challenges.interview.src.zoo.animal import Animal


class Reptile(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = False
        self.vertebrate = True
        self.eatMe = 'crunch ... crunch ...'
    # TODO - implement this class!

    def is_warm_blooded(self):
        return self.warm_blooded

    def is_vertebrate(self):
        return self.vertebrate

    def eat(self):
        return self.eatMe
