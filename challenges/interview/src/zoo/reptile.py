from challenges.interview.src.zoo.animal import Animal


class Reptile(Animal):
    """this is our Reptile class"""
    # TODO - implement this class!
    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = False


    # examples ... using @property later
    def is_warm_blooded(self):
        return not self.warm_blooded


    # all mammals have specialized teeth ... they eat differently!
    # @override
    def eat(self):
        return 'crunch ... crunch ...'
