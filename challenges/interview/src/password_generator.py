import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!

        Alpha = "qwertyuiopasdfghjklzxcvbnm"
        Digits = "0123456789"
        Symbols = "!@#$%^&*()"
        Password = ''
        for c in range(5):
            Password += random.choice(Alpha)
        for c in range(4):
            Password += random.choice(Digits)
        Password += random.choice(Symbols)

        return Password
