import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        p = re.compile('cat')  # p is a regex string
        m = p.search(s)  # you are trying to find p in s
        # if m is none, there are no matches
        if m is None:
            return False
        else:
            return True


    @staticmethod
    def alphanumeric_glyph(s):
        # TODO - implement this method!
        p = re.compile('cat')  # p is a regex string
        m = p.search(s)  # you are trying to find p in s
        # if m is none, there are no matches
        if m is None:
            return False
        else:
            return True

    @staticmethod
    def avoid_nile_crocodile(s):
        # TODO - implement this method!
        p = re.compile('crocodile')  # p is a regex string
        m = p.search(s)  # you are trying to find p in s
        # if m is none, there are no matches
        if m is None:
            return True
        else:
            return False

    @staticmethod
    def find_gold_scarab(s):
        # TODO - implement this method!
        p = re.compile('gold scarab')  # p is a regex string
        m = p.match(s)  # you are trying to find p in s
        # if m is none, there are no matches
        if m is None:
            return False
        else:
            return True

    @staticmethod
    def raid_tuts_tomb(s):
        # TODO - implement this method!
        p = re.compile('tut|TUT|Tut|tUt')  # p is a regex string
        m = p.search(s)  # you are trying to find p in s
        # if m is none, there are no matches
        if m is None:
            return False
        else:
            return True

    @staticmethod
    def steal_crystal_skull(s):
        # TODO - implement this method!
        return
