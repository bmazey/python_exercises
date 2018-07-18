class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):
        backwards = s[::-1]
        if s == backwards:
            return True
        else:
            return False
