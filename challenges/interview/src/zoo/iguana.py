from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
    """this is our public Iguana class, which 'extends' Reptile"""
    def __init__(self, name):
        super().__init__(name)
        self.size = 3
        self.legs = 4
        self.color = 'green'
    # TODO - implement this class!

    def get_size(self):
        return self.size

    def get_legs(self):
        return self.legs

    def get_color(self):
        return self.color
