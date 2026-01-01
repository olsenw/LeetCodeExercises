# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An integer divisible by the sum of its digits is said to be a Harshad
    number. Given an integer x, return the sum of the digits of x if x is a
    Harshad number, otherwise return -1.
    '''
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        h = x
        a = 0
        while h:
            a += h % 10
            h //= 10
        if x % a == 0:
            return a
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 18
        o = 9
        self.assertEqual(s.sumOfTheDigitsOfHarshadNumber(i), o)

    def test_two(self):
        s = Solution()
        i = 23
        o = -1
        self.assertEqual(s.sumOfTheDigitsOfHarshadNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)