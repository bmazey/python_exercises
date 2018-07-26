import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        # TODO - implement this method!
        return re.match(r'(.*)cat(.*)', s)

    @staticmethod
    def alphanumeric_glyph(s):
        # TODO - implement this method!
        return re.match(r'[a-z]{4}[0-9]{5,7}', s)

    @staticmethod
    def avoid_nile_crocodile(s):
        # TODO - implement this method!
        return not re.match (r'(.*)crocodile(.*)', s)

    @staticmethod
    def find_gold_scarab(s):
        # TODO - implement this method!
        return

    @staticmethod
    def raid_tuts_tomb(s):
        # TODO - implement this method!
        return

    @staticmethod
    def steal_crystal_skull(s):
        # TODO - implement this method!
        return
