import exercises.patterns.builder.car_builder as car_builder


class CarBuilderDirector(object):

    @staticmethod
    def construct_suv():
        # TODO - implement this method!
        builder = car_builder.CarBuilder()
        builder.set_color('yellow')
        return builder.get_result()

    @staticmethod
    def construct_sports_car():
        # TODO - implement this method!
        builder = car_builder.CarBuilder()
        builder.set_doors(2)
        builder.set_fuel('premium gas')
        builder.set_color('red')
        return builder.get_result()

    @staticmethod
    def construct_eighteen_wheeler():
        # TODO - implement this method!
        b = car_builder.CarBuilder()
        b.set_wheels(18)
        b.set_doors(2)
        b.set_fuel('diesel')
        b.set_color('blue')
        return b.get_result()

    @staticmethod
    def construct_tesla():
        # TODO - implement this method!
        c = car_builder.CarBuilder()
        c.set_fuel('electricity')
        return c.get_result()


# Let's try it out below ...
car = CarBuilderDirector.construct_suv()
print(car)
