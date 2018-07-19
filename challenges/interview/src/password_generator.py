import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    # TODO - implement this method!

    @staticmethod
    def generate_password():
        chars = 'abcdefghijklmnopqrstuvwxyz'
        password = ''
        for i in range(5):
            password += random.choice(chars)
        chars2 = '0123456789'
        for i in range(6, 10):
            password += random.choice(chars2)
        chars3 = '!@#$%^&*'
        for i in range(10, 11):
            password += random.choice(chars3)
        print(password)

        chars = 'abcdefghijklmnopqrstuvwxyz'
        password2 = ''
        for i in range(5):
            password2 += random.choice(chars)
        chars2 = '0123456789'
        for i in range(6, 10):
            password2 += random.choice(chars2)
        chars3 = '!@#$%^&*'
        for i in range(10, 11):
            password2 += random.choice(chars3)

        if password == password2:
            chars = 'abcdefghijklmnopqrstuvwxyz'
        password2 = ''
        for i in range(5):
            password2 += random.choice(chars)
        chars2 = '0123456789'
        for i in range(6, 10):
            password2 += random.choice(chars2)
        chars3 = '!@#$%^&*'
        for i in range(10, 11):
            password2 += random.choice(chars3)
            return password2

