from exercises.patterns.builder.car_builder import CarBuilder


class CarBuilderDirector(object):

    @staticmethod
    def construct_suv():
        # instantiates suv
        suv = CarBuilder()
        # sets color to yellow
        suv.set_color('yellow')
        return suv.get_result()

    @staticmethod
    def construct_sports_car():
        # TODO - implement this method!
        # instantiates sports car
        sports = CarBuilder()
        # sets number of doors to 2
        sports.set_doors(2)
        # sets fuel to 'premium gas'
        sports.set_fuel('premium gas')
        # sets color to red
        sports.set_color('red')
        return sports.get_result()

    @staticmethod
    def construct_eighteen_wheeler():
        # TODO - implement this method!
        # instantiates eighteen wheeler
        wheeler = CarBuilder()
        # sets wheels to 18
        wheeler.set_wheels(18)
        # sets number of doors to 2
        wheeler.set_doors(2)
        # sets fuel to diesel
        wheeler.set_fuel('diesel')
        # sets color to blue
        wheeler.set_color('blue')
        return wheeler.get_result()

    @staticmethod
    def construct_tesla():
        # TODO - implement this method!
        # instantiates tesla
        tesla = CarBuilder()
        # sets fuel to electricity
        tesla.set_fuel('electricity')
        return tesla.get_result()


# Let's try it out below ...
# car = CarBuilderDirector.construct_suv()
# print(car)
