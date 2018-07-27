import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    # any character, then cat, then any character
    @staticmethod
    def worship_sacred_cats(s):
        cat = re.match(r'.*cat+.*', s)
        return cat

    # any letter 4 times, then any number 5-7 times
    @staticmethod
    def alphanumeric_glyph(s):
        glyph = re.match(r'[a-z]{4}[0-9]{5,7}', s)
        return glyph

    # anything without crocodile
    @staticmethod
    def avoid_nile_crocodile(s):
        return not re.search(r'crocodile', s)
        # croc = re.match(r'[^c]', s)
        # return croc

    # anything with 'gold scarab' return 'gold', else return false
    @staticmethod
    def find_gold_scarab(s):
        if re.match(r'gold+\s+scarab+', s):
            return 'gold'
        else:
            return False

    # anything with tut (lower or upper case) is false
    @staticmethod
    def raid_tuts_tomb(s):
        return not re.search(r'tut', s, re.I)

    # substitute skull for idol
    @staticmethod
    def steal_crystal_skull(s):
        return re.sub('skull', 'idol', s)
