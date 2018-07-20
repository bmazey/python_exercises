class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):
        # evaluates if the forward is equivalent to the reverse
        if s == s[::-1]:
            return True
        else:
            return False
