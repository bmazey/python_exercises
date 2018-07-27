import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        # TODO - implement this method! test
        matchObj= re.match(r"(.*)(cat+)(.*)", s)
        return matchObj

    @staticmethod
    def alphanumeric_glyph(s):
        # TODO - implement this method!
        match = re.match(r"[a-z]{3}(d)[0-9]{4,10}", s)
        return match

    @staticmethod
    def avoid_nile_crocodile(s):
        # TODO - implement this method!
        a = re.match(r'(nile)*', s)
        if re.search(r'crocodile', s):
            return False
        else:
            return a

    @staticmethod
    def find_gold_scarab(s):
        # TODO - implement this method!
        if re.match('gold scarab', s):
            return 'gold'
        else:
            return False

    @staticmethod
    def raid_tuts_tomb(s):
        # TODO - implement this method!
        match = re.match('(tomb)*(/s)*', s, re.I)
        if re.search(r'[Tt][Uu][Tt]', s):
            return False
        else:
            return match

    @staticmethod
    def steal_crystal_skull(s):
        # TODO - implement this method!
        yeet = re.sub(r'skull', "idol", s)
        return yeet
