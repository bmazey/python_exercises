

class Bakery(object):
    def __init__(self, desserts):
        self.desserts = desserts

    def __len__(self):
        return len(self.desserts)

    def __add__(self, bakery):
        return Bakery(self.desserts + bakery.desserts)

    def __getitem__(self, item):
        return self.desserts[item]

