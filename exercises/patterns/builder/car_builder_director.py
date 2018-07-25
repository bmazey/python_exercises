from exercises.patterns.builder.car_builder import CarBuilder


class CarBuilderDirector(object):

    @staticmethod
    def construct_suv():
        # TODO - implement this method!
        builder = CarBuilder()
        builder.set_wheels(4)
        builder.set_doors(4)
        builder.set_color('yellow')
        builder.set_fuel('unleaded gas')
        return builder.get_result()

    @staticmethod
    def construct_sports_car():
        # TODO - implement this method!
        builder = CarBuilder()
        builder.set_wheels(4)
        builder.set_doors(2)
        builder.set_color('red')
        builder.set_fuel('premium gas')
        return builder.get_result()

    @staticmethod
    def construct_eighteen_wheeler():
        # TODO - implement this method!
        builder = CarBuilder()
        builder.set_wheels(18)
        builder.set_doors(2)
        builder.set_color('blue')
        builder.set_fuel('diesel')
        return builder.get_result()

    @staticmethod
    def construct_tesla():
        # TODO - implement this method!
        builder = CarBuilder()
        builder.set_wheels(4)
        builder.set_doors(4)
        builder.set_color('black')
        builder.set_fuel('electricity')
        return builder.get_result()


# Let's try it out below ...
# car = CarBuilderDirector.construct_suv()
# print(car)
