class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    # TODO - implement this method!

    def is_palindrome(s):
        s = str(s)
        a = s[::-1]
        if a != s:
            return False
        else:
            return True

    print(is_palindrome)














