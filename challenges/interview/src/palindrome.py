class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):
        # turns word 's' backwards
        backwards = s[::-1]
        # if 's' is the same backwards and forwards, then 's' is a palindrome
        if s == backwards:
            return True
        else:
            return False
