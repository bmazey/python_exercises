class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):
        if(s[::-1] == s):
            return True
        else:
            return False
