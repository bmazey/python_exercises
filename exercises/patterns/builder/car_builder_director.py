import exercises.patterns.builder.car_builder

class CarBuilderDirector(object):

    @staticmethod
    def construct_suv():
        # TODO - implement this method!
        suv = exercises.patterns.builder.car_builder.CarBuilder()
        suv.set_wheels(4)
        suv.set_doors(4)
        suv.set_fuel('unleaded gas')
        suv.set_color('yellow')
        return suv.get_result()

    @staticmethod
    def construct_sports_car():
        # TODO - implement this method!
        sports_car = exercises.patterns.builder.car_builder.CarBuilder()
        sports_car.set_wheels(4)
        sports_car.set_doors(2)
        sports_car.set_fuel('premium gas')
        sports_car.set_color('red')
        return sports_car.get_result()

    @staticmethod
    def construct_eighteen_wheeler():
        # TODO - implement this method!
        eighteen_wheeler = exercises.patterns.builder.car_builder.CarBuilder()
        eighteen_wheeler.set_wheels(18)
        eighteen_wheeler.set_doors(2)
        eighteen_wheeler.set_fuel('diesel')
        eighteen_wheeler.set_color('blue')
        return eighteen_wheeler.get_result()

    @staticmethod
    def construct_tesla():
        # TODO - implement this method!
        tesla = exercises.patterns.builder.car_builder.CarBuilder()
        tesla.set_wheels(4)
        tesla.set_doors(4)
        tesla.set_fuel('electricity')
        tesla.set_color('black')
        return tesla.get_result()


# Let's try it out below ...
# car = CarBuilderDirector.construct_suv()
# print(car)
