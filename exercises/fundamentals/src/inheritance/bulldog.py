from exercises.fundamentals.src.inheritance.dog import Dog


class Bulldog(Dog):
    def __init__(self, name):
        super().__init__(name)
        # bulldogs are stocky, have short ears and have a color
        self.size = 3
        self.color = 'brindle'
        self.ear_size = 1

    # bulldogs growl
    def bark(self):
        return "growl ... growl ... : " + self.name

    def size(self):
        return self.size
