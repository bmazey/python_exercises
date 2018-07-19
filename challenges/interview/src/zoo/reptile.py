from challenges.interview.src.zoo.animal import Animal


class Reptile(Animal):

    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = False
        self.size = 3
        self.legs = 4
        self.color = 'green'

    def is_warm_blooded(self):
        return self.warm_blooded

    def eat(self):
        return 'crunch ... crunch ...'

    # TODO - implement this class!
