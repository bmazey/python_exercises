import exercises.patterns.builder.car_builder


class CarBuilderDirector(object):

    @staticmethod
    def construct_suv():
        # creates yellow suv with 4 wheels 4 doors and unleaded gas
        suv = exercises.patterns.builder.car_builder.CarBuilder()
        suv.set_wheels(4)
        suv.set_doors(4)
        suv.set_fuel('unleaded gas')
        suv.set_color('yellow')
        return suv.get_result()

    @staticmethod
    def construct_sports_car():
        # creates red sports car with 4 wheels 2 doors and premium gas
        sc = exercises.patterns.builder.car_builder.CarBuilder()
        sc.set_wheels(4)
        sc.set_doors(2)
        sc.set_fuel('premium gas')
        sc.set_color('red')
        return sc.get_result()

    @staticmethod
    def construct_eighteen_wheeler():
        # creates blue eighteen wheeler with 18 wheels 2 doors and diesel
        ew = exercises.patterns.builder.car_builder.CarBuilder()
        ew.set_wheels(18)
        ew.set_doors(2)
        ew.set_fuel('diesel')
        ew.set_color('blue')
        return ew.get_result()

    @staticmethod
    def construct_tesla():
        # creates black tesla with 4 wheels 4 doors and electricity
        tes = exercises.patterns.builder.car_builder.CarBuilder()
        tes.set_wheels(4)
        tes.set_doors(4)
        tes.set_fuel('electricity')
        tes.set_color('black')
        return tes.get_result()


# Let's try it out below ...
# car = CarBuilderDirector.construct_suv()
# print(car)
