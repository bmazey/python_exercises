class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):
        # TODO - implement this method!

        if s == s[::-1]:
            return True
        else:
            return False
