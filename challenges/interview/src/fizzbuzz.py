class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # test
    @staticmethod
    def fizzbuzz(i):
        # TODO - implement this method!


        # test method! test
        string = ''

        if i % 15 == 0 :
            string = 'fizzbuzz'
        elif i % 3 == 0 :
            string = 'fizz'
        elif i % 5 == 0 :
            string = 'buzz'

        return string
