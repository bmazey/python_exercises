import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        # TODO - implement this method!
        cat = re.search('cat', s)
        return cat

    @staticmethod
    def alphanumeric_glyph(s):
        # TODO - implement this method!
        glyph = re.search(r'[a-z]{4}[0-9]+', s)
        return glyph

    @staticmethod
    def avoid_nile_crocodile(s):
        # TODO - implement this method!
        croc = re.search('crocodile', s)
        return not croc

    @staticmethod
    def find_gold_scarab(s):
        # TODO - implement this method!
        gold = re.search('gold scarab', s)
        if gold:
            return 'gold'

    @staticmethod
    def raid_tuts_tomb(s):
        # TODO - implement this method!
        return not re.search('tut', s.casefold())

    @staticmethod
    def steal_crystal_skull(s):
        # TODO - implement this method!
        skull = (re.sub('skull', 'idol', s))
        return skull
