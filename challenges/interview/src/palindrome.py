class Palindrome(object):
    @staticmethod
    def is_palindrome(s):
        string = ''
        for i in s:
            string = i + string
        if string == s:
            return True
        return False
