# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The power of an integer x is defined as the number of steps needed to
    transform x into 1 using the following steps:
    * if x is even then x = x / 2
    * if x is odd then x = 3 * x + 1

    Given three integers lo, hi and k. The task is to sort all integers in the
    interval [lo, hi] by the power value in ascending order, if two or more
    integers have the same power value sort them by ascending order.

    Return the kth integer in the range [lo, hi] sorted by the power value.

    Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will
    transform into 1 using these steps and that the power of x wil fit in a
    32-bit signed integer.
    '''
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def dp(i:int) -> int:
            if i == 1:
                return 0
            if i % 2:
                return 1 + dp(3 * i + 1)
            else:
                return 1 + dp(i // 2)
        s = sorted(range(lo,hi+1), key=lambda x:(dp(x),x))
        return s[k-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 12
        j = 15
        k = 2
        o = 13
        self.assertEqual(s.getKth(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 7
        j = 11
        k = 4
        o = 7
        self.assertEqual(s.getKth(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)