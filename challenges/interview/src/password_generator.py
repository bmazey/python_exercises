import random

class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!
        letters = 'abcdefghijklmnopqrstuvwxyz'
        numbers = '123456789'
        symbols = '!@#$%^&*'
        password = ''
        for i in range (5):
            password = password + random.choice(letters)

        for i in range(4):
            password = password + random.choice(numbers)

        for i in range(1):
            password = password + random.choice(symbols)

        return password
