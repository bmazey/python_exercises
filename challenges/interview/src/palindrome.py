class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):
        # TODO - implement this method!
        a = s[::-1]
        if a == s:
            return True
        else:
            return False

