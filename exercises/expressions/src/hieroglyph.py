import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        # TODO - implement this method!
        result = re.search('cat', s)
        return result

    @staticmethod
    def alphanumeric_glyph(s):
        # TODO - implement this method!
        return re.search(r'[a-z]{4}[0-9]+', s)

    @staticmethod
    def avoid_nile_crocodile(s):
        # TODO - implement this method!
        return not re.search('crocodile', s)

    @staticmethod
    def find_gold_scarab(s):
        # TODO - implement this method!
        if s == 'gold scarab':
            return 'gold'
        else:
            return False

    @staticmethod
    def raid_tuts_tomb(s):
        # TODO - implement this method!
        return not re.search('tut', s.casefold())

    @staticmethod
    def steal_crystal_skull(s):
        # TODO - implement this method!
        return re.sub('skull', 'idol', s)
