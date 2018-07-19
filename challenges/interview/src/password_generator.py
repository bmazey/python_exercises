import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    # creates a bank of characters to be used in the generate_password() function
    @staticmethod
    def generate_password():
        letters = 'abcdefghijklmnopqrstuvwxyz'
        numbers = '1234567890'
        misc = '!@#$%^&*'
        password = ''
        password = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters)\
                    + random.choice(letters) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers)\
                    + random.choice(numbers) + random.choice(misc)
        return password
