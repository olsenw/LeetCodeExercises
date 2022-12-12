# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a staircase with n steps. It is possible to go up 1 or 2 steps at a
    time. How many distinct ways are there to climb to the top of the stairs?
    '''
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        stairs = [0] * (n+1)
        stairs[1] = 1
        stairs[2] = 2
        for i in range(3, n+1):
            stairs[i] = stairs[i-1] + stairs[i-2]
        return stairs[n]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.climbStairs(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 2
        self.assertEqual(s.climbStairs(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = 3
        self.assertEqual(s.climbStairs(i), o)

    def test_45(self):
        s = Solution()
        i = 45
        o = 1836311903
        self.assertEqual(s.climbStairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)