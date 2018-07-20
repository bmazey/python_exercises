import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!
        password = ''
        for things in range (0,5):
            password = password + random.choice('qwertyuiopasdfghjklzxcvbnm')
        for things in range (5,9):
            password = password + random.choice('123456789')
        for things in range (9,10):
            password = password + random.choice('!@#$%^&*')

        return password
