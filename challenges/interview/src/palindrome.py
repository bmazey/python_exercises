class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):
        # TODO - implement this method!
        # creating a string that is s backwards
        string = s[::-1]

        #testing to see if the string is equal to s
        if(string == s):
            return True
        else:
            return False