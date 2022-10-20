# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Roman numerals are represented by the following symbols:
    *   I =    1
    *  IV =    4
    *   V =    5
    *  IX =    9
    *   X =   10
    *  XL =   40
    *   L =   50
    *  XC =   90
    *   C =  100
    *  CD =  400
    *   D =  500
    *  CM =  900
    *   M = 1000
    Written largest value to smallest value from left to right.

    Given an integer convert it to a roman numeral
    '''
    def intToRoman_case_statements(self, num: int) -> str:
        s = ""
        while num:
            if num >= 1000:
                num -= 1000
                s += 'M'
            elif num >= 900:
                num -= 900
                s += 'CM'
            elif num >= 500:
                num -= 500
                s += 'D'
            elif num >= 400:
                num -= 400
                s += 'CD'
            elif num >= 100:
                num -= 100
                s += 'C'
            elif num >= 90:
                num -= 90
                s += 'XC'
            elif num >= 50:
                num -= 50
                s += 'L'
            elif num >= 40:
                num -= 40
                s += 'XL'
            elif num >= 10:
                num -= 10
                s += 'X'
            elif num >= 9:
                num -= 9
                s += 'IX'
            elif num >= 5:
                num -= 5
                s += 'V'
            elif num >= 4:
                num -= 4
                s += 'IV'
            else:
                num -= 1
                s += 'I'
        return s

    def intToRoman_while_list(self, num: int) -> str:
        s = ""
        c = [(1,'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
        while num:
            if num >= c[-1][0]:
                num -= c[-1][0]
                s += c[-1][1]
            else:
                c.pop()
        return s

    d = [(1,'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
    def intToRoman(self, num: int) -> str:
        s = ""
        i = len(self.d) - 1
        while num:
            if num >= self.d[i][0]:
                num -= self.d[i][0]
                s += self.d[i][1]
            else:
                i -= 1
        return s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        o = "III"
        self.assertEqual(s.intToRoman(i), o)

    def test_two(self):
        s = Solution()
        i = 58
        o = "LVIII"
        self.assertEqual(s.intToRoman(i), o)

    def test_three(self):
        s = Solution()
        i = 1994
        o = "MCMXCIV"
        self.assertEqual(s.intToRoman(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)