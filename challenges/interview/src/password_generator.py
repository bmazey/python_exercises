import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        numbers = '0123456789'
        symbols = '!@#$%^&*'
        password = ''

        i = 0
        while i < 5:
            password += alphabet[random.randint(0, len(alphabet)-1)]
            i+=1

        j = 0
        while j < 4:
            password += numbers[random.randint(0, len(numbers)-1)]
            j+=1


        password += symbols[random.randint(0, len(symbols)-1)]


        return password









