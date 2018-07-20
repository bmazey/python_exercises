class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):
        result = ''
        for i in range(len(s)):
            result += s[len(s)-i-1]

        if result == s:
            return True
        else:
            return False



