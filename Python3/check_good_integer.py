# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n.

    Let digitSum be the sum of the digits of n, and let squareSum be the sum of
    the squares of the digits of n.

    An integer is called good if squareSum - digitSum >= 50.

    Return true if n is good. Otherwise, return false.
    '''
    def checkGoodInteger(self, n: int) -> bool:
        digitSum = 0
        squareSum = 0
        while n > 0:
            d = n % 10
            n = n // 10
            digitSum += d
            squareSum += d * d
        return squareSum - digitSum >= 50

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1000
        o = False
        self.assertEqual(s.checkGoodInteger(i), o)

    def test_two(self):
        s = Solution()
        i = 19
        o = True
        self.assertEqual(s.checkGoodInteger(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)