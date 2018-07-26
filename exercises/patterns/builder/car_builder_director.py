import exercises.patterns.builder.car_builder


class CarBuilderDirector(object):

    @staticmethod
    def construct_suv():
        builder = exercises.patterns.builder.car_builder.CarBuilder()
        builder.set_color('yellow')
        builder.set_wheels(4)
        builder.set_doors(4)
        builder.set_fuel('unleaded gas')
        return builder.get_result()

    @staticmethod
    def construct_sports_car():
        sportscar = exercises.patterns.builder.car_builder.CarBuilder()
        sportscar.set_color('red')
        sportscar.set_wheels(4)
        sportscar.set_doors(2)
        sportscar.set_fuel('premium gas')
        return sportscar.get_result()

    @staticmethod
    def construct_eighteen_wheeler():
        # TODO - implement this method!
        builder = exercises.patterns.builder.car_builder.CarBuilder()
        builder.set_color('blue')
        builder.set_wheels(18)
        builder.set_doors(2)
        builder.set_fuel('diesel')
        return builder.get_result()

    @staticmethod
    def construct_tesla():
        # TODO - implement this method!
        builder = exercises.patterns.builder.car_builder.CarBuilder()
        builder.set_color('black')
        builder.set_wheels(4)
        builder.set_doors(4)
        builder.set_fuel('electricity')
        return builder.get_result()

# Let's try it out below ...
# car = CarBuilderDirector.construct_suv()
# print(car)
