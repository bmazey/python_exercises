import random
import string

class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        password = ''.join([random.choice(string.ascii_lowercase)  for _ in range(5)])
        password += ''.join([random.choice(string.digits) for _ in range(4)])
        password += random.choice('!@#$%^&*')
        return password

