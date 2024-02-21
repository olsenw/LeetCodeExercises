# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers left and right that represent the range [left, right],
    return the bitwise AND of all numbers in this range, inclusive.
    '''
    def rangeBitwiseAnd_brute(self, left: int, right: int) -> int:
        a = left
        for i in range(left, right+1):
            a &= i
        return a

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        a = 0
        i = 1 << 30
        while i:
            if left & i != right & i:
                break
            if left & i:
                a |= i
            i >>= 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = 7
        o = 4
        self.assertEqual(s.rangeBitwiseAnd(i,j), o)

    def test_two(self):
        s = Solution()
        i = 0
        j = 0
        o = 0
        self.assertEqual(s.rangeBitwiseAnd(i,j), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = 2147483647
        o = 0
        self.assertEqual(s.rangeBitwiseAnd(i,j), o)

    def test_four(self):
        s = Solution()
        i = 2147483000
        j = 2147483647
        o = 2147482624
        self.assertEqual(s.rangeBitwiseAnd(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)