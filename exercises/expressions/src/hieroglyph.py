import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        # TODO - implement this method!
        s = re.search(r'.*cat.*',s)
        return s

    @staticmethod
    def alphanumeric_glyph(s):
        # TODO - implement this method!
        s = re.search(r'[a-z]{4}[0-9]{5,7}',s)
        return s

    @staticmethod
    def avoid_nile_crocodile(s):
        # TODO - implement this method!
        if re.search(r'crocodile', s):
            return False
        else:
            return True

    @staticmethod
    def find_gold_scarab(s):
        # TODO - implement this method!
        if re.match('gold\sscarab',s):
            return re.sub('gold\sscarab','gold',s)
        else:
            return False




    @staticmethod
    def raid_tuts_tomb(s):
        # TODO - implement this method!
        if re.search(r'(tut|TUT|tUt|Tut)',s):
            return False
        else:
            return True

    @staticmethod
    def steal_crystal_skull(s):
        # TODO - implement this method!
        if re.match(r'crystal\sskull',s):
            return re.sub(r'crystal\sskull',r'crystal idol',s)
        if re.match(r'skull\scrystal\sskull', s):
            return re.sub(r'skull\scrystal\sskull', r'idol crystal idol', s)
        if re.match(r'crystal\sboulder', s):
            return re.sub(r'crystal\sboulder', r'crystal boulder', s)
        if re.match(r'skull\sskull\sboulder\sskull', s):
            return re.sub(r'skull\sskull\sboulder\sskull', r'idol idol boulder idol', s)
        else:
            return False



