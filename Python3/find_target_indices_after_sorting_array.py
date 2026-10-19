# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums and a target element target.

    A target index is an index i such that nums[i] == target.

    Return a list of the target indices of nums after sorting nums in
    non-decreasing order. If there are no target indices, return an empty list.
    The returned list must be sorted in increasing order.
    '''
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i in range(len(nums)) if nums[i] == target]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,5,2,3]
        j = 2
        o = [1,2]
        self.assertEqual(s.targetIndices(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,5,2,3]
        j = 3
        o = [3]
        self.assertEqual(s.targetIndices(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,5,2,3]
        j = 5
        o = [4]
        self.assertEqual(s.targetIndices(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)