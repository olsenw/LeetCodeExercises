# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a non-negative integer x, return the square root of x rounded down to
    the nearest integer. The returned integer should be non-negative as well.

    Do not use a built-in exponent function or operator. (ie pow(x, 0.5))
    '''
    # needed help correcting binary search
    # https://leetcode.com/problems/sqrtx/solutions/3317131/4-lines-of-code-binary-search-approach-and-normal-approach/
    # missing early cut out... tied to use only single if/else
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        i,j = 1, x
        while i <= j:
            k = i + (j - i) // 2
            if k * k == x:
                return k
            if k * k > x:
                j = k - 1
            else:
                i = k + 1
        return j

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        o = 2
        self.assertEqual(s.mySqrt(i), o)

    def test_two(self):
        s = Solution()
        i = 8
        o = 2
        self.assertEqual(s.mySqrt(i), o)

    def test_three(self):
        s = Solution()
        for i in range(10000):
            self.assertEqual(s.mySqrt(i), pow(i,0.5)//1)

if __name__ == '__main__':
    unittest.main(verbosity=2)