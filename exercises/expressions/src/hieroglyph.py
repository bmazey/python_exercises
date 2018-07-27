import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        return re.match(r'(.*)cat(.*)', s)
        # TODO - implement this method!

    @staticmethod
    def alphanumeric_glyph(s):
        # TODO - implement this method!
        return re.match(r'[a-z]{4}[0-9*]', s)


    @staticmethod
    def avoid_nile_crocodile(s):
        # TODO - implement this method!
        return not(re.match(r'(.*)crocodile(.*)', s))

    @staticmethod
    def find_gold_scarab(s):
        # TODO - implement this method!
        matches = re.match(r'gold(?= scarab)', s)
        if matches:
            return matches.group()
        else:
            return False


    @staticmethod
    def raid_tuts_tomb(s):
        # TODO - implement this method!
        return not re.match(r'(.*)(t|T)(U|u)(t|T)(.*)', s)

    @staticmethod
    def steal_crystal_skull(s):
        # TODO - implement this method!
        result = s.replace('skull', 'idol')
        return result
