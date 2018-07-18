from challenges.interview.src.zoo.animal import Animal


class Reptile(Animal):
    """this is our Reptile class"""
    # TODO - implement this class!
    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = False

    def is_warm_blooded(self):
        return self.warm_blooded

    def eat(self):
        return 'crunch ... crunch ...'
