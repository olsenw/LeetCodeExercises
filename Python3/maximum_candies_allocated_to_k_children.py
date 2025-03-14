# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array candies. Each element in the array denotes a
    pile of candies of size[i]. It is possible to divide each pile into any
    number of sub piles, but it is impossible to merge two piles together.

    Also given an integer k. Allocate piles of candies to k children such that
    each child gets the same number of candies. Each child can be allocated
    candies from only one pile of candies and some piles of candies may go
    unused.

    Return the maximum number of candies each child can get.
    '''
    def maximumCandies(self, candies: List[int], k: int) -> int:
        i,j = 0,10**7
        while i < j:
            m = i + ((j - i) // 2) + 1
            pass
            if sum(n//m for n in candies) >= k:
                i = m
            else:
                j = m - 1
        return j

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,8,6]
        j = 3
        o = 5
        self.assertEqual(s.maximumCandies(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,5]
        j = 11
        o = 0
        self.assertEqual(s.maximumCandies(i,j), o)

    def test_three(self):
        s = Solution()
        i = [4,7,5]
        j = 4
        o = 3
        self.assertEqual(s.maximumCandies(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)