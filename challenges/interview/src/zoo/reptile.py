from challenges.interview.src.zoo.animal import Animal


class Reptile(Animal):
    """this is our Reptile class"""
    # TODO - implement this class!
    def __init__(self,name):
        self.warmblooded = False

    def is_warm_blooded(self):
        return self.warmblooded

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_legs(self):
        return self.legs