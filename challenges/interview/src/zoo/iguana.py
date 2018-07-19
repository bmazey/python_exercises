from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
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

    def eat(self):
        return 'crunch ... crunch ...'
    # TODO - implement this class!
