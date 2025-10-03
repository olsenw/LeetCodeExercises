# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums, return the smallest index i of nums
    such that i mod 10 == nums[i], or -1 if such index does not exist.

    x mod y denotes the remainder when x is divided by y.
    '''
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,2]
        o = 0
        self.assertEqual(s.smallestEqual(i), o)

    def test_two(self):
        s = Solution()
        i = [4,3,2,1]
        o = 2
        self.assertEqual(s.smallestEqual(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5,6,7,8,9,0]
        o = -1
        self.assertEqual(s.smallestEqual(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)