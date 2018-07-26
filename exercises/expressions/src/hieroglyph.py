import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        # TODO - implement this method!
        match = re.match('(.)*cat(.)*', s)
        return match

    @staticmethod
    def alphanumeric_glyph(s):
        # TODO - implement this method!
        match = re.match(r'[a-z]{4}[0-9]{5,7}', s)
        return match

    @staticmethod
    def avoid_nile_crocodile(s):
        # TODO - implement this method!
        search = re.search(r'crocodile', s)
        return not search

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
        search = re.search(r'tut', s.casefold())
        return not search

    @staticmethod
    def steal_crystal_skull(s):
        # TODO - implement this method!
        sub = re.sub(r'skull', 'idol', s)
        return sub
