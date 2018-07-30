import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):

        return re.match(r'(.*)cat(.*)', s)
    # , s: see if the expression exists in a string

    @staticmethod
    def alphanumeric_glyph(s):

        return re.match(r'[a-z]{4}[0-9]{5,7}', s)

    @staticmethod
    def avoid_nile_crocodile(s):

        return not(re.match(r'(.*)(crocodile)+', s))

    @staticmethod
    def find_gold_scarab(s):
        new_s = str.replace(r'(gold)/(?=scarab)', 'gold')
        if s == 'gold scarab':
            return 'gold'
        else:
            return False


    @staticmethod
    def raid_tuts_tomb(s):
        return not re.match(r'((.*)(tut)+)', s, re.IGNORECASE)

    @staticmethod
    def steal_crystal_skull(s):
            # return re.match(r'(crystal)*/(boulder)*/(skull)*', s)
            new_s = re.sub(r'skull', 'idol', s)
            return new_s

