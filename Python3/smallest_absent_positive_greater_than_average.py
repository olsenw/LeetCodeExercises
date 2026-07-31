# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from math import ceil
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    Return the smallest absent positive integer in nums such that it is strictly
    greater than the average of all elements in nums.

    The average of an array is defined as the sum of all its elements divided by
    the number of elements.
    '''
    def smallestAbsent(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        a = max(ceil(s / n) + (s % n == 0), 1)
        s = set(nums)
        while a in s:
            a += 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,5]
        o = 6
        self.assertEqual(s.smallestAbsent(i), o)

    def test_two(self):
        s = Solution()
        i = [-1,1,2]
        o = 3
        self.assertEqual(s.smallestAbsent(i), o)

    def test_three(self):
        s = Solution()
        i = [4,-1]
        o = 2
        self.assertEqual(s.smallestAbsent(i), o)

    def test_four(self):
        s = Solution()
        i = [-4,-5,-6]
        o = 1
        self.assertEqual(s.smallestAbsent(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)