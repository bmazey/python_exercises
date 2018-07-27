import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        # returns true if it includes the word cat
        return re.match(r'.*cat+.*', s, re.I)

    @staticmethod
    def alphanumeric_glyph(s):
        # returns true if 4 letters and then 5 or 7 numbers
        return re.match(r'[a-z]{4}[0-9]{5,7}', s, re.I)

    @staticmethod
    def avoid_nile_crocodile(s):
        # returns true if no existence of the word crocodile
        return not re.search(r'crocodile', s)

    @staticmethod
    def find_gold_scarab(s):
        # returns string 'gold' if s only possesses 'gold's and 'scarab's in that order. Else, false
        if re.match(r'gold+ scarab+', s):
            return 'gold'
        else:
            return False

    @staticmethod
    def raid_tuts_tomb(s):
        # returns true when s has no existence of the word 'tut'
        return not re.search(r'tut', s, re.I)

    @staticmethod
    def steal_crystal_skull(s):
        # replaces all instances of the word skull with idol
        return re.sub(r'skull', 'idol', s)
