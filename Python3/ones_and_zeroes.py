# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from functools import cache

class Solution:
    '''
    Given an array of binary strings strs and two integers m and n.

    Return the size of the largest subset of strs such that there are at
    most m 0's and n 1's in the subset.

    A set x is a subset of a set y if all elements of x are also
    elements of y.
    '''
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        d = []
        for s in strs:
            a = 0
            for c in s:
                a += ord(c)
            a -= ord("0") * len(s)
            d.append([len(s) - a, a])
        @cache
        def sub(index, zeros, ones):
            if index == len(strs):
                return 0
            if zeros + d[index][0] <= m and ones + d[index][1] <= n:
                a = 1 + sub(index + 1, zeros + d[index][0], ones + d[index][1])
                b = sub(index + 1, zeros, ones)
                return max(a, b)
            else:
                return sub(index + 1, zeros, ones)
        return sub(0, 0, 0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["10","0001","111001","1","0"]
        j = 5
        k = 3
        o = 4
        self.assertEqual(s.findMaxForm(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = ["10","0","1"]
        j = 1
        k = 1
        o = 2
        self.assertEqual(s.findMaxForm(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = ["10","0001","111001","1","0"]
        j = 50
        k = 50
        o = 5
        self.assertEqual(s.findMaxForm(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)