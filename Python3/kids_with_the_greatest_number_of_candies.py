# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n kids with candies. Given an integer array candies, where each
    candies[i] represents the number of candies the ith kid has, and an integer
    extraCandies, denoting the number of extra candies available.

    Return a boolean array result of length n, where result[i] is true if, after
    giving the ith kid all the extraCandies, they will have the greatest number
    of candies among all the kids, or false otherwise.

    Note that multiple kids can have the greatest number of candies.
    '''
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [c + extraCandies >= m for c in candies]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,5,1,3]
        j = 3
        o = [True,True,True,False,True]
        self.assertEqual(s.kidsWithCandies(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,2,1,1,2]
        j = 1
        o = [True,False,False,False,False]
        self.assertEqual(s.kidsWithCandies(i,j), o)

    def test_three(self):
        s = Solution()
        i = [12,1,12]
        j = 10
        o = [True,False,True]
        self.assertEqual(s.kidsWithCandies(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)