# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, move all 0's to the end of it while maintaining
    the relative order of the non-zero elements.

    Note that this must be done in-place without copying the array.
    '''
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        while i < len(nums) and nums[i] != 0:
            i += 1
        j = i + 1
        while j < len(nums):
            while j < len(nums) and nums[j] == 0:
                j += 1
            else:
                if j < len(nums) and nums[i] == 0:
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,0,3,12]
        o = [1,3,12,0,0]
        s.moveZeroes(i)
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = [0]
        o = [0]
        s.moveZeroes(i)
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5,6]
        o = [1,2,3,4,5,6]
        s.moveZeroes(i)
        self.assertEqual(i, o)

    def test_three(self):
        s = Solution()
        i = [0,0,0]
        o = [0,0,0]
        s.moveZeroes(i)
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)