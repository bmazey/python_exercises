class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):
        if s[0, -1] == s[-1, 0]:
            return True
        else:
            return False
