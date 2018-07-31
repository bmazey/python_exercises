from exercises.patterns.builder.car_builder import CarBuilder


class CarBuilderDirector(object):
    @staticmethod
    def construct_suv():
        builder = CarBuilder()
        builder.set_color('yellow')
        return builder.get_result()

    @staticmethod
    def construct_sports_car():
        builder = CarBuilder()
        builder.set_color('red')
        builder.set_fuel('premium gas')
        builder.set_doors(2)
        return builder.get_result()

    @staticmethod
    def construct_eighteen_wheeler():
        builder = CarBuilder()
        builder.set_color('blue')
        builder.set_fuel('diesel')
        builder.set_wheels(18)
        builder.set_doors(2)
        return builder.get_result()

    @staticmethod
    def construct_tesla():
        builder = CarBuilder()
        builder.set_color('black')
        builder.set_fuel('electricity')
        return builder.get_result()



# Let's try it out below ...
# car = CarBuilderDirector.construct_suv()
# print(car)
