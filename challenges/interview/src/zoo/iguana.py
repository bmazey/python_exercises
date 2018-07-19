from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
    def __init__(self, name):
        super().__init__(name)
        self.color = 'green'
        self.size = 3
        self.legs = 4

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_legs(self):
        return self.legs
