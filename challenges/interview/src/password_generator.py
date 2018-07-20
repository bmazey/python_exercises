import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!
        password = ''

        char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        symb = '!@#$%^&*'
        for i in range(5):
            a = random.randint(0,25)
            password += char[a]
        for i in range(4):
            a = random.randint(0,8)
            password += str(a)
        for i in range(1):
            a = random.randint(0,7)
            password += symb[a]

        return password
