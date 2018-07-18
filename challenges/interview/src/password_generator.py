import random
import string


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!
        password = ''
        i = 0
        while i < 5:
            password += random.choice(string.ascii_letters)
            i += 1
        i = 0
        while i < 4:
            password += str(random.randint(0, 9))
            i += 1
        password += "!"
        return password
