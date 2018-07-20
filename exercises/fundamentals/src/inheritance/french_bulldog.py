from exercises.fundamentals.src.inheritance.bulldog import Bulldog


class FrenchBulldog(Bulldog):
    def __init__(self, name):
        super().__init__(name)
        # french bulldogs are smaller, but have larger ears
        self.size = 2
        self.ear_size = 4

    # french bulldogs yip!
    def bark(self):
        return "yip! ... yip! ... : " + str(self.name)
