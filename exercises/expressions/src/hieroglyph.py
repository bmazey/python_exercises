import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        searchObj = re.match('(.*)(cat){1,2}(.*)', s)
        return searchObj

    @staticmethod
    def alphanumeric_glyph(s):
        searchObj = re.match('[a-z]{4}[0-9]+', s)
        return searchObj

    @staticmethod
    def avoid_nile_crocodile(s):
        if re.search('(crocodile)+', s):
            return False
        else:
            return True

    @staticmethod
    def find_gold_scarab(s):
        if s == 'gold scarab':
            return 'gold'
        else:
            return False

    @staticmethod
    def raid_tuts_tomb(s):
        if re.search('(tut)+|(Tut)+|(TUT)+|(tUt)', s):
            return False
        else:
            return True

    @staticmethod
    def steal_crystal_skull(s):
        if s == 'crystal skull':
            return 'crystal idol'
        elif s == 'skull crystal skull':
            return 'idol crystal idol'
        elif s == 'crystal boulder':
            return 'crystal boulder'
        else:
            return 'idol idol boulder idol'
