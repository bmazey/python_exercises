from exercises.patterns.builder.car_builder import *


class CarBuilderDirector(object):

    @staticmethod
    def construct_suv():
        # TODO - implement this method!

        car_builder = CarBuilder()
        car_builder.set_wheels(4)
        car_builder.set_doors(4)
        car_builder.set_fuel('unleaded gas')
        car_builder.set_color('yellow')

        return car_builder.get_result()

    @staticmethod
    def construct_sports_car():
        # TODO - implement this method!

        car_builder = CarBuilder()
        car_builder.set_wheels(4)
        car_builder.set_doors(2)
        car_builder.set_fuel('premium gas')
        car_builder.set_color('red')

        return car_builder.get_result()

    @staticmethod
    def construct_eighteen_wheeler():
        # TODO - implement this method!

        car_builder = CarBuilder()
        car_builder.set_wheels(18)
        car_builder.set_doors(2)
        car_builder.set_fuel('diesel')
        car_builder.set_color('blue')

        return car_builder.get_result()

    @staticmethod
    def construct_tesla():
        # TODO - implement this method!

        car_builder = CarBuilder()
        car_builder.set_wheels(4)
        car_builder.set_doors(4)
        car_builder.set_fuel('electricity')
        car_builder.set_color('black')

        return car_builder.get_result()



# Let's try it out below ...
# car = CarBuilderDirector.construct_suv()
# print(car)
