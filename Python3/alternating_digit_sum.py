# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n. Each digit of n has a sign according to the
    following rules:
    * The most significant digit is assigned a positive sign.
    * Each other digit has an opposite sign to its adjacent digits.

    Return the sum of all digits with their corresponding sign.
    '''
    def alternateDigitSum_str(self, n: int) -> int:
        a = 0
        b = True
        for s in str(n):
            if b:
                a += int(s)
            else:
                a -= int(s)
            b = not b
        return a

    def alternateDigitSum(self, n: int) -> int:
        x,y,z = 0,0,0
        while n:
            n,a = divmod(n, 10)
            if z % 2:
                x += a
                y -= a
            else:
                x -= a
                y += a
            z += 1
        return y if z % 2 else x

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 521
        o = 4
        self.assertEqual(s.alternateDigitSum(i), o)

    def test_two(self):
        s = Solution()
        i = 111
        o = 1
        self.assertEqual(s.alternateDigitSum(i), o)

    def test_three(self):
        s = Solution()
        i = 886996
        o = 0
        self.assertEqual(s.alternateDigitSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)