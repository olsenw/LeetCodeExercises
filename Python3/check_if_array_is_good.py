# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. It is considered a good array if it is a
    permutation of an array base[n].

    base[n] = [1,2,...,n-1,n,n] (in other words, it is an array of length n + 1
    which contains 1 to n -1 exactly once, plus two occurrences of n).

    Return true if the given array is good, otherwise return false.
    '''
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)-1
        nums.sort()
        pass
        return n == nums[-1] and n == nums[-2] and nums[:-1] == list(range(1,n+1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2, 1, 3]
        o = False
        self.assertEqual(s.isGood(i), o)

    def test_two(self):
        s = Solution()
        i = [1, 3, 3, 2]
        o = True
        self.assertEqual(s.isGood(i), o)

    def test_three(self):
        s = Solution()
        i = [1, 1]
        o = True
        self.assertEqual(s.isGood(i), o)

    def test_four(self):
        s = Solution()
        i = [3, 4, 4, 1, 2, 1]
        o = False
        self.assertEqual(s.isGood(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)