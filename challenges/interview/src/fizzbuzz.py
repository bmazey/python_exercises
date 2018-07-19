class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # test
    @staticmethod
    def fizzbuzz(i):

        if i % 15 == 0:
            return 'fizzbuzz'

        if i % 3 == 0:
            return 'fizz'
        elif i % 5 == 0:
            return 'buzz'
        else:
            return 'nope'

# tes