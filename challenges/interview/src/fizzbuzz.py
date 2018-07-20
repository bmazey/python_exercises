class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # test
    @staticmethod
    def fizzbuzz(i):
        # TODO - implement this method!
        if i % 3 == 0 and i % 5 != 0:
            return "fizz"
        elif  i % 5 == 0 and i % 3 != 0:
            return "buzz"
        elif  i % 5 == 0 and i % 3 == 0:
            return "fizzbuzz"
