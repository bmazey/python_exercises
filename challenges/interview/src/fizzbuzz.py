class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # TODO - implement this method!
    # test method! test
    @staticmethod
    def fizzbuzz(i):
        string = ''
        if i % 3 == 0 and i % 5 == 0:
            string = 'fizzbuzz'
        elif i % 3 == 0:
            string = 'fizz'
        elif i % 5 == 0:
            string = 'buzz'
        else:
            string = str(i)
        return string
