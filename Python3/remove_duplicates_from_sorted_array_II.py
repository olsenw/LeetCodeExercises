# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums sorted in non-decreasing order, remove
    some duplicates in-place such that each unique element appears at
    most twice. The relative order should be kept the same.

    Since it is impossible to change the length of the array in some
    languages, instead have the result be placed in the first part of
    the array nums. Formally, if there are k elements after removing the
    duplicates, then the first k elements should hold the final result.
    It does not matter what you leave beyond the first k elements.

    Return k after placing the final result i the first k slots of nums.

    Do not allocate extra space for another array. Modify the input
    array in-place with O(1) extra memory.
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        last = nums[0]
        count = 1
        k = 1
        i = 1
        while i < len(nums):
            if nums[i] != last:
                last = nums[i]
                count = 1
            else:
                count += 1
            nums[k] = nums[i]
            if count < 3:
                k += 1
            i += 1
        return k

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,1,2,2,3]
        i2 = [1,1,2,2,3]
        o = 5
        n = s.removeDuplicates(i)
        self.assertEqual(n, o)
        for j in range(n):
            self.assertEqual(i[j], i2[j])

    def test_two(self):
        s = Solution()
        i = [0,0,1,1,1,1,2,3,3]
        i2 = [0,0,1,1,2,3,3]
        o = 7
        n = s.removeDuplicates(i)
        self.assertEqual(n, o)
        for j in range(n):
            self.assertEqual(i[j], i2[j])

if __name__ == '__main__':
    unittest.main(verbosity=2)