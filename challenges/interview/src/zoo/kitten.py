from challenges.interview.src.zoo.mammal import Mammal


class Kitten(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.size = 1
        self.callMe = 'meow ... meow ...'
        self.color = 'orange'

    def color(self):
        return self.color

    def size(self):
        return self.size

    def call(self):
        return self.callMe
