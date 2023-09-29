# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An array is monotonic if it is either monotone increasing or monotone
    decreasing.

    An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
    An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

    Given an integer array nums, return true if the given array is monotonic, or
    false otherwise.
    '''
    def isMonotonic(self, nums: List[int]) -> bool:
        l = (lambda x, y : x <= y) if nums[0] <= nums[-1] else (lambda x, y : x >= y)
        for i,j in zip(nums[:-1],nums[1:]):
            if not l(i,j):
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,3]
        o = True
        self.assertEqual(s.isMonotonic(i), o)

    def test_two(self):
        s = Solution()
        i = [6,5,4,4]
        o = True
        self.assertEqual(s.isMonotonic(i), o)

    def test_three(self):
        s = Solution()
        i = [1,3,2]
        o = False
        self.assertEqual(s.isMonotonic(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)