import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():

        password = ''

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        chars = ['!', '@', '#', '$', '%', '^', '&', '*']

        for i in range(5):
            password += str(letters[random.randint(0, 25)])

        for i in range(4):
            password += str(nums[random.randint(0, 9)])

        password += str(chars[random.randint(0, 7)])

        return password
