from challenges.interview.src.zoo.animal import Animal


class Reptile(Animal):
    """this is our Reptile class"""
    # TODO - implement this class!

    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = False
        self.size = 3
        self.legs = 4
        self.color = 'green'

    def is_warm_blooded(self):
        return self.warm_blooded

    def get_size(self):
        return self.size

    def get_legs(self):
        return self.legs

    def get_color(self):
        return self.color

    @property
    def eat(self):
        return 'crunch ... crunch'

