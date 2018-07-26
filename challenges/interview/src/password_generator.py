import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!

        alpha = 'abcdefghijklmnopqrstuvwxyz'
        digits = '123456789'
        symbols = '!@#$%^&*'
        password = ''

        for c in range(10):
            password1 = random.choice(alpha) + random.choice(alpha) + random.choice(alpha) + random.choice(
                alpha) + random.choice(alpha) + random.choice(digits) + random.choice(digits) + random.choice(
                digits) + random.choice(digits) + random.choice(symbols)
        return(password1)

