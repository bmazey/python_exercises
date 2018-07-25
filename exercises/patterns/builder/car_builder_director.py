import exercises.patterns.builder.car_builder


class CarBuilderDirector(object):

    @staticmethod
    def construct_suv():
        suv = exercises.patterns.builder.car_builder.CarBuilder()
        suv.set_wheels(4)
        suv.set_doors(4)
        suv.set_fuel('unleaded gas')
        suv.set_color('yellow')
        return suv.get_result()

    @staticmethod
    def construct_sports_car():
        car = exercises.patterns.builder.car_builder.CarBuilder()
        car.set_wheels(4)
        car.set_doors(2)
        car.set_fuel('premium gas')
        car.set_color('red')
        return car.get_result()

    @staticmethod
    def construct_eighteen_wheeler():
        ew = exercises.patterns.builder.car_builder.CarBuilder()
        ew.set_wheels(18)
        ew.set_doors(2)
        ew.set_fuel('diesel')
        ew.set_color('blue')
        return ew.get_result()

    @staticmethod
    def construct_tesla():
        tesla = exercises.patterns.builder.car_builder.CarBuilder()
        tesla.set_wheels(4)
        tesla.set_doors(4)
        tesla.set_fuel('electricity')
        tesla.set_color('black')
        return tesla.get_result()


# Let's try it out below ...
# car = CarBuilderDirector.construct_suv()
# print(car)
