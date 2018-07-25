from exercises.patterns.builder.car_builder import CarBuilder


class CarBuilderDirector(object):

    @staticmethod
    def construct_suv():

        suv = CarBuilder()

        suv.set_wheels(4)
        suv.set_doors(4)
        suv.set_fuel('unleaded gas')
        suv.set_color('yellow')

        return suv.get_result()

    @staticmethod
    def construct_sports_car():

        sport = CarBuilder()

        sport.set_wheels(4)
        sport.set_doors(2)
        sport.set_fuel('premium gas')
        sport.set_color('red')

        return sport.get_result()

    @staticmethod
    def construct_eighteen_wheeler():

        truck = CarBuilder()

        truck.set_wheels(18)
        truck.set_doors(2)
        truck.set_fuel('diesel')
        truck.set_color('blue')

        return truck.get_result()

    @staticmethod
    def construct_tesla():

        tesla = CarBuilder()

        tesla.set_wheels(4)
        tesla.set_doors(4)
        tesla.set_fuel('electricity')
        tesla.set_color('black')

        return tesla.get_result()


# Let's try it out below ...
# car = CarBuilderDirector.construct_suv()
# print(car)
