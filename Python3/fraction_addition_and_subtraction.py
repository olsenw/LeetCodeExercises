# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string expression representing an expression of fraction addition
    and subtraction, return the calculation result in string format.

    The final result should be an irreducible fraction. If the final result is
    an integer, change it to the format of a fraction that has a denominator 1.
    So in this case, 2 should be converted to 2/1.
    '''
    def fractionAddition(self, expression: str) -> str:
        numerator, denominator = 0, 1
        n,d = 0, 1
        addition = True
        divisor = False
        for e in expression:
            if e == '+' or e == '-':
                if addition:
                    numerator = (numerator * d) + (n * denominator)
                else:
                    numerator = (numerator * d) - (n * denominator)
                denominator = denominator * d
                m = math.gcd(numerator, denominator)
                numerator, denominator = numerator // m, denominator // m
                addition = e == '+'
                divisor = False
                n = 0
            elif e == '/':
                divisor = True
            else:
                if not divisor:
                    n = (n * 10) + int(e)
                    d = 0
                else:
                    d = (d * 10) + int(e)
        if addition:
            numerator = (numerator * d) + (n * denominator)
        else:
            numerator = (numerator * d) - (n * denominator)
        denominator = denominator * d
        m = math.gcd(numerator, denominator)
        numerator, denominator = numerator // m, denominator // m
        return f'{numerator}/{denominator}'

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "-1/2+1/2+1/3"
        o = "1/3"
        self.assertEqual(s.fractionAddition(i), o)

    def test_two(self):
        s = Solution()
        i = "-1/2+1/2"
        o = "0/1"
        self.assertEqual(s.fractionAddition(i), o)

    def test_three(self):
        s = Solution()
        i = "1/3-1/2"
        o = "-1/6"
        self.assertEqual(s.fractionAddition(i), o)

    def test_four(self):
        s = Solution()
        i = "3/2+1/2"
        o = "2/1"
        self.assertEqual(s.fractionAddition(i), o)

    def test_five(self):
        s = Solution()
        i = "3/2+1/2+1/3"
        o = "7/3"
        self.assertEqual(s.fractionAddition(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)