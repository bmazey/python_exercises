class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):
        # TODO - implement this method!
        s = str(s)
        a = s[::-1]
        if a != s:
            return False
        else:
            return True

