import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        set1 = 'abcdefghijklmnopqrstuvwxyz'
        set2 = '1234567890'
        set3 = '!@#$%^&*'
        password = ''
        for password1 in range(5):
            password += random.choice(set1)
        for password2 in range(4):
            password += random.choice(set2)
        for password3 in range(1):
            password += random.choice(set3)

        return password

