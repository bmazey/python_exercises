from exercises.fundamentals.src.inheritance.bulldog import Bulldog


class FrenchBulldog(Bulldog):
    def __init__(self, name):
        super().__init__(name)
        # french bulldogs are smaller, but have larger ears
        self.size = 2
        self.ear_size = 4
        self._collar = 'blue'

    # french bulldogs yip!
    def bark(self):
        return "yip! ... yip! ... : " + str(self.name)

    @property
    def collar(self):
        return self._collar

    @collar.setter
    def collar(self, value):
        # if value == 'yellow':
            # print("french bulldogs won't wear yellow collars!")
            # self._collar = 'blue'
        self._collar = value

    @collar.deleter
    def collar(self):
        # remove collar
        del self._collar

    @staticmethod
    def walk():
        return "let's go to Central Park!"
