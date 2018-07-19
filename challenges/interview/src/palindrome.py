class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):

        yes = ''

        for i in s:
            yes = i + s

        if s == yes:
            return True
        else:
            return False

