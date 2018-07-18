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
            password += alpha[random.randint(26)]

        for x in range(4) :
            password += random.randint(10)

        password += sym[random.randint(8)]

        return password
