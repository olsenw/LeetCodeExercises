# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers n and x. Construct an array of positive integers nums of
    size n where for every 0 <= 1 < n - 1, nums[i + 1] is greater than nums[i],
    and the result of the bitwise AND operation between all elements of nums is
    x.

    Return the minimum possible value of nums[n - 1]
    '''
    # trying to use hints
    def minEnd_fails(self, n: int, x: int) -> int:
        a = x
        for _ in range(n-1):
            i = 1
            while i & a == i:
                i <<= 1
            a |= i
        return a

    # bit magic, lot of trial and error to get pattern
    def minEnd(self, n: int, x: int) -> int:
        a = x
        i = 1
        while a & i == i:
            i <<= 1
        for j in range(32):
            b = 1 << j
            if (n - 1) & b == b:
                a |= i 
            i <<= 1
            while a & i == i:
                i <<= 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3,4
        o = 6
        self.assertEqual(s.minEnd(*i), o)

    def test_two(self):
        s = Solution()
        i = 2,7
        o = 15
        self.assertEqual(s.minEnd(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)