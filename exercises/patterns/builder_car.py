class Car:
    def __init__(self,wheels,doors,fuel,color):
        self.wheels = wheels
        self.doors = doors
        self.fuel = fuel
        self.color = color

    def __str__(self):
        return "This is a {} car with {} wheels and {} doors. " \
               "It runs on {}.".format(self.color, self.wheels, self.doors, self.fuel)


cars = [] # 50 sports cars, 50 wheels,
