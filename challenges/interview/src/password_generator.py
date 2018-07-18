import random
import string

class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        password = ''
        symbols = '!@#$%^&*'
        for i in range(10):
            if i<5:
                password += string.ascii_lowercase[random.randint(0,25)]
            elif i>4 and i<9:
                password += str(random.randint(0,9))
            elif i>=9:
                password += symbols[random.randint(0,len(symbols)-1)]
        return password
