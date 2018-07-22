from exercises.fundamentals.src.inheritance.dog import Dog


class Dalmatian(Dog):
    def __init__(self, name):
        super().__init__(name)
        # dalmatians are mid-sized dogs with white fur and black spots
        self.color = 'black'
