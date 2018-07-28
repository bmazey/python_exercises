import exercises.patterns.builder.car_builder as car_builder


class CarBuilderDirector(object):

    @staticmethod
    def construct_suv():
        suv = car_builder.CarBuilder()
        suv.set_color('yellow')
        return suv.car

    @staticmethod
    def construct_sports_car():
        sports_car = car_builder.CarBuilder()
        sports_car.set_doors(2)
        sports_car.set_fuel('premium gas')
        sports_car.set_color('red')
        return sports_car.car

    @staticmethod
    def construct_eighteen_wheeler():
        wheeler = car_builder.CarBuilder()
        wheeler.set_wheels(18)
        wheeler.set_doors(2)
        wheeler.set_fuel('diesel')
        wheeler.set_color('blue')
        return wheeler.car

    @staticmethod
    def construct_tesla():
        tesla = car_builder.CarBuilder()
        tesla.set_fuel('electricity')
        return tesla.car

# Let's try it out below ...
# car = CarBuilderDirector.construct_suv()
# print(car)
