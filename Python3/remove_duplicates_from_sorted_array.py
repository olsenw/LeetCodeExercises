# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums sorted in non-decreasing order, remove the
    duplicates in-place such that each unique element appears only once. The
    relative order of the elements should be kept the same.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. This problem should be solved
    in-place with O(1) extra memory.
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            nums[j] = nums[i]
            j += 1
        return j

class UnitTesting(unittest.TestCase):
    '''
    Did testing on Leetcode due to special test code.
    '''
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)