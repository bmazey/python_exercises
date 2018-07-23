class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # test
    @staticmethod
    def fizzbuzz(i):
        # TODO - implement this method!

        if i%3 == 0 and i%5 == 0:  # Testing both multiples
            return "fizzbuzz"

        elif i%3 == 0:  # Testing only 3
            return "fizz"

        elif i%5 == 0:  # Testing only 5
            return "buzz"

