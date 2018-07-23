class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # test comment
    @staticmethod
    def fizzbuzz(i):
        # if i is a multiple of 15 it evaluates fizzbuzz
        if i % 15 == 0:
            return 'fizzbuzz'
        # if i is a multiple of 5 it evaluates buzz
        elif i % 5 == 0:
            return 'buzz'
        # if i is a multiple of 3 it evaluates fizz
        elif i % 3 == 0:
            return 'fizz'
        # if it isn't a multiple of 15, 5, or 3 it evaluates the original number
        else:
            return i
