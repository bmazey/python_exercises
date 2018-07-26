

class Pizza(object):
    def __init__(self, toppings):
        self.toppings = toppings

    def __len__(self):
        return len(self.toppings)

    def __getitem__(self, position):
        return self.toppings[position]

    def __add__(self, other):
        return Pizza(self.toppings + other.toppings)




