import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        # TODO - implement this method!
        s = re.match(r'.*cat.*',s)
        return s

    @staticmethod
    def alphanumeric_glyph(s):
        # TODO - implement this method!
        s = re.match(r'[a-z]{4}[0-9]{5,7}',s)
        return s

    @staticmethod
    def avoid_nile_crocodile(s):
        # TODO - implement this method!
        word = re.match(r'nile*',s)
        if re.search(r'crocodile',s):
            return False
        else:
            return word

    @staticmethod
    def find_gold_scarab(s):
        if re.match(r'gold+\s+scarab+', s):
            return 'gold'
        else:
            return False

    @staticmethod
    def raid_tuts_tomb(s):
        # TODO - implement this method!
        w = re.search('tut',s.casefold())
        return not w

    @staticmethod
    def steal_crystal_skull(s):
        # TODO - implement this method!
        a = re.sub('skull', 'idol', s)
        return a
