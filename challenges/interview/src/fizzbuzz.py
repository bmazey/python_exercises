class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # test
    @staticmethod
    def fizzbuzz(i):
        # my first comment
        # TODO - implement this method!

        string = ''
        # if i is a multiple of 15, return fizzbuzz
        if i % 15 == 0:
            string = "fizzbuzz"
        # if i is a multiple of 5, return buzz
        elif i % 5 == 0:
            string = "buzz"
        # if i is a multiple of 3, return fizz
        elif i % 3 == 0:
            string = "fizz"

        return string
