import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        # TODO - implement this method!
        return re.match(r'(.*)(cat)(.*)', s)

    @staticmethod
    def alphanumeric_glyph(s):
        # TODO - implement this method!
        return re.match(r'[a-z]{4}[0-9]{5,7}', s)

    @staticmethod
    def avoid_nile_crocodile(s):
        a = re.match(r'(nile)*', s)
        if re.search(r'(crocodile)',s):
            return False
        else:
            return a

    @staticmethod
    def find_gold_scarab(s):
        if re.search(r'(gold scarab)',s):
            return 'gold'
        else:
            return False

    @staticmethod
    def raid_tuts_tomb(s):
        a = re.match(r'(tomb)*(/s)*', s)
        if re.search(r'[Tt][Uu][Tt]', s, re.I):
            return False
        else:
            return a

    @staticmethod
    def steal_crystal_skull(s):
        a = re.sub(r'skull', "idol", s)
        return a
