import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!

        # change one element in the password
        password = 'ASDFG123' + str(random.randint(1 , 9)) + '%'
        return password
