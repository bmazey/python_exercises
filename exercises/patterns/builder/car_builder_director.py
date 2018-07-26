from exercises.patterns.builder.car_builder import CarBuilder


class CarBuilderDirector(object):
    @staticmethod
    def construct_suv():
        car1 = CarBuilder()
        def set_wheels(self, 4):
            self.car.wheels = 4

        def set_doors(self, 4):
            self.car.doors = 4

        def set_fuel(self, 'unleaded gas'):
            self.car.fuel = 'unleaded gas'

        def set_color(self, 'yellow'):
            self.car.color = 'yellow'

        def get_result(self):
            return self.car1

    @staticmethod
    def construct_sports_car(self):
        # TODO - implement this method!
        car = CarBuilderDirector.construct_suv(self, wheels=4, doors=2, fuel='premium gas', color='')
        print(car)
        self.wheels = 4
        self.doors = 2
        self.fuel = 'premium gas'
        self.color = 'red'
        return

    @staticmethod
    def construct_eighteen_wheeler(self):
        super(CarBuilder)
        self.wheels = 18
        self.doors = 2
        self.fuel = 'diesel'
        self.color = 'blue'
        # TODO - implement this method!
        return

    @staticmethod
    def construct_tesla(self):
        super(CarBuilder)
        self.wheels = 4
        self.doors = 4
        self.fuel = 'electricity'
        self.color = 'black'
        # TODO - implement this method!
        return


# Let's try it out below ...
# car = CarBuilderDirector.construct_suv()
# print(car)
