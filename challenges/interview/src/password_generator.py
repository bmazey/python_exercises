import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!

        password = ''
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for x in range(5):
            password = password + random.choice(alpha)

        for x in range(4):
            password = password + str(random.randint(0, 10))

        symbol = '!@#$%^&*'
        password = password + random.choice(symbol)

         return password
