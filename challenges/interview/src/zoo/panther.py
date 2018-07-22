from challenges.interview.src.zoo.mammal import Mammal


class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""
    def __init__(self,name):
        super().__init__(name)
        self.size = 5
        self.legs = 4
        self.color = 'black'

    def call(self):
        return 'ROAR!'
    

