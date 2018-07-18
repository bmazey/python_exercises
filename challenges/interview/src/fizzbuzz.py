class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # test
    # hello!
    @staticmethod
    def fizzbuzz(i):
        # TODO - implement this method!
        if i % 15 == 0:
            string = 'fizzbuzz'
        elif i % 5 == 0:
            string = 'buzz'
        elif i % 3 == 0:
            string = 'fizz'
        else:
            string = ''

        return string


