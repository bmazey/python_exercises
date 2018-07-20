from challenges.interview.src.zoo.animal import Animal


class Reptile(Animal):
    """this is our Reptile class"""
    # TODO - implement this class!
    def __init__(self, name):
        self.name = name
        self.warm_blooded = False

    # all Animals eat
    def eat(self):
        return "crunch ... crunch ..."

    def is_warm_blooded(self):
        return self.warm_blooded

    def get_color(self):
        return 'green'

    def get_size(self):
        return 3

    def get_legs(self):
        return 4
