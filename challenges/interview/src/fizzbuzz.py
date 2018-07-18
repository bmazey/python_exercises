class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # test
    @staticmethod
    def fizzbuzz(i):
        # my first comment
        # TODO - implement this method!

        string = ''
        if i % 15 == 0:
            string = "fizzbuzz"
        elif i % 5 == 0:
            string = "buzz"
        elif i % 3 == 0:
            string = "fizz"

        return string
