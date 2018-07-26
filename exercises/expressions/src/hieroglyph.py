import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        # checks if string contains 'cat'
        match = re.match('(.*)(cat*)(.*)', s)
        return match

    @staticmethod
    def alphanumeric_glyph(s):
        # checks if string contains 4 letters followed with at least one number
        match = re.match('[a-zA-Z]{4}([0-9]+)', s)
        return match

    @staticmethod
    def avoid_nile_crocodile(s):
        # checks if you find one or more 'crocodile' in the string
        # if match= true, returns !match
        match = re.search('(crocodile+)', s)
        return not match

    @staticmethod
    def find_gold_scarab(s):
        # checks if string is exactly 'gold scarab'
        match = re.match('(gold scarab)', s)
        if match:
            return 'gold'

    @staticmethod
    def raid_tuts_tomb(s):
        # searches for keyword 'tut' ignoring case
        # if 'tut' appears, return !match
        match = re.search('(tut)', s, re.IGNORECASE)
        return not match

    @staticmethod
    def steal_crystal_skull(s):
        # searches for 'skull' and replaces with 'idol'
        # returns substituted version of string
        match = re.sub('(skull)', 'idol', s)
        return match
