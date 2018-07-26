import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!

        alpha = 'qwertyuiopasdfghjklzxcvbnm'
        sym = '!@#$%^&*'

        password = ''

        for x in range(5) :
            password += alpha[random.randint(0, 25)]

        for x in range(4) :
            password += str(random.randint(0, 9))

        password += sym[random.randint(0, 7)]

        return password
