from challenges.interview.src.sweets.dessert import Dessert


class Brownie(Dessert):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def get_brownie_size(self):
        return 'brownie size:' + str(self.size)

