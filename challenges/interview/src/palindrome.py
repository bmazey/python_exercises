class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):
        # TODO - implement this method!
        if s[::-1] == s:
            return True
        return False
