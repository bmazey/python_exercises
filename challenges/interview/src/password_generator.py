import random
import string


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!
        password = ''

        # randomizes 5 alphabetical characters to add to password
        for i in range(0, 5):
            password += random.choice(string.ascii_letters)
            i += 1
        # randomizes 4 numbers to add to password
        for i in range(0,4):
            password += str(random.randint(0, 9))
            i += 1

        # randomizes a symbol and adds it to password
        symbols = ['!', '@' , '#' , '$' , '%','^','&','*']
        password += symbols[random.randint(0, 7)]

        print(password)

        return password
