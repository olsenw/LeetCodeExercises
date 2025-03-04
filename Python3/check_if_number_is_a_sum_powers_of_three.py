# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, return true if it is possible to represent n as the sum
    of distinct powers of three. Otherwise, return false.

    An integer y is a power of three if there exists an integer such that
    y == 3^x.
    '''
    # note hint 1) max power is 3**16
    def checkPowersOfThree_backtracking(self, n: int) -> bool:
        power = [3**i for i in range(17)]
        @cache
        def dp(n, i):
            if n == 0:
                return True
            if i == len(power) or n < power[i]:
                return False
            return any(dp(n-power[i], i+1) for i in range(i,17))
        return dp(n, 0)

    # based on leetcode ternary representation solution
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 12
        o = True
        self.assertEqual(s.checkPowersOfThree(i), o)

    def test_two(self):
        s = Solution()
        i = 91
        o = True
        self.assertEqual(s.checkPowersOfThree(i), o)

    def test_three(self):
        s = Solution()
        i = 21
        o = False
        self.assertEqual(s.checkPowersOfThree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)