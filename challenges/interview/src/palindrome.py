class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):

        return s[::-1] == s
