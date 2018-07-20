from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    def __init__(self,name):
        super().__init__(name)
        self.legs = 4
        self.size = 5
        self.color = 'black'

    def call(self):
        return 'ROAR!'
