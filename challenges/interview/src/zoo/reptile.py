from challenges.interview.src.zoo.animal import Animal


class Reptile(Animal):
    """this is our Reptile class"""
    # TODO - implement this class!

    # initializes reptile class
    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = False
        self.vertebrate = True

    # method to call warm_blooded attribute
    def is_warm_blooded(self):
        return self.warm_blooded

    # method to call vertebrate attribute
    def is_vertebrate(self):
        return self.vertebrate

    # all Reptile have specialized teeth ... they eat differently!
    # @override
    def eat(self):
        return 'munch ... munch ...'
