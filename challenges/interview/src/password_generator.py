import random
import string

class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!

        password = ''
        alpha = 'qwertyuiopasdfghjklzxcvbnm'
        for x in range(0,5):
            password += random.choice(alpha)

        alpha = '1234567890'
        for x in range(0,4):
            password += random.choice(alpha)

        alpha = '!@#$%^&*'
        for x in range(0,1):
            password += random.choice(alpha)

        return password
