import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!

        x = random.randint(0, 9)
        y = random.randint(0, 9)

        password = 'abcde' + "12" + str(x) + str(y) + "*"

        return password



