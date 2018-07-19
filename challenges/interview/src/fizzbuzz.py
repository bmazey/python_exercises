class FizzBuzz(object):
    @staticmethod
    def fizzbuzz(i):
        string = ''
        if i % 3 == 0 and i % 5 == 0:
            string = 'fizzbuzz'
        elif i % 3 == 0:
            string = 'fizz'
        elif i % 5 == 0:
            string = 'buzz'
        return string
