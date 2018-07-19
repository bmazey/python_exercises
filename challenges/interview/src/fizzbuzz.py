class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # test
    @staticmethod
    def fizzbuzz(i):
        # TODO - implement this method!
        string = ''

        if i % 3 == 0:
            string += 'fizz'
        if i % 5 == 0:
            string += 'buzz'

        return string
