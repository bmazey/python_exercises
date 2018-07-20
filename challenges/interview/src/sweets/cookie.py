from challenges.interview.src.sweets.dessert import Dessert


class Cookie(Dessert):
    def __init__(self, name):
        super().__init__(name)
        self.flavor = 'chocolate chip'

