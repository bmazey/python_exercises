import random
import string


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!

        symbols = {'!', '@', '#', '$', '%', '^', '&', '*'}
        password = ''
        for i in range(0, 4):
            password += str(random.choice(string.letters))

        for x in range(0, 3):
            password += random.randint(0, 9)

        password += random.choice(symbols)

        return password
