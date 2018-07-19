import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!
        password = ''
        letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = "1234567890"
        symbols = "!@#$%^&*"

        for x in range(5):
            password += random.choice(letters)
        for x in range(4):
            password += random.choice(numbers)
        password += random.choice(symbols)


        return password
