import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        return re.match(r'(.*)cat(.*)', s)

    @staticmethod
    def alphanumeric_glyph(s):
        return re.match(r'[a-z]{4}[0-9]{5,7}', s)

    @staticmethod
    def avoid_nile_crocodile(s):
        return not re.match(r'(.*)crocodile(.*)', s)

    @staticmethod
    def find_gold_scarab(s):
        matches = re.match(r'gold(?= scarab)', s)
        if matches:
            return matches.group()
        else:
            return False

    @staticmethod
    def raid_tuts_tomb(s):
        return not re.match(r'(.*)tut(.*)', s, re.I)
        # return re.match(r'tomb', s) or re.match(r'(tomb )', s) or re.match(r'tomb( tomb)*', s)

    @staticmethod
    def steal_crystal_skull(s):
        s = s.replace('skull', 'idol')
        return s
