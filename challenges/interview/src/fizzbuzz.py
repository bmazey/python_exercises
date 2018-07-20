class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # test
    @staticmethod
    def fizzbuzz(i):
        if (i%3 == 0):
            it = 'fizz'
        if (i%5 == 0):
            it = 'buzz'
        if (i%15 ==0):
            it ='fizzbuzz'
        return it
