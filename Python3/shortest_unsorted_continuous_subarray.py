# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums, find the one continuous subarray that
    if sorted in ascending order, then the whole array will sorted in
    ascending order.

    Return the shortest such subarray and output its length.
    '''
    def findUnsortedSubarray_brute_sort(self, nums: List[int]) -> int:
        s = sorted(nums)
        i = 0
        for i in range(len(nums)):
            if s[i] != nums[i]:
                break
        j = len(nums) - 1
        if i == j:
            return 0
        for j in range(len(nums) - 1, -1, -1):
            if s[j] != nums[j]:
                break
        return j - i + 1

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        # find left bound (where it descends)
        while i < j and nums[i] <= nums[i + 1]:
            i += 1
        # array is sorted
        if i == j:
            return 0
        # find right bound (where it ascends)
        while j > 0 and nums[j - 1] <= nums[j]:
            j -= 1
        # find minimum and maximum between the bounds
        m = min(nums[i:j+1])
        n = max(nums[i:j+1])
        # lower left bound if larger than minimum
        while i > 0 and nums[i - 1] > m:
            i -= 1
        # increase right bound if less than maximum
        while j < len(nums) - 1 and nums[j + 1] < n:
            j += 1
        # index math
        return j - i + 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,6,4,8,10,9,15]
        o = 5
        self.assertEqual(s.findUnsortedSubarray(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        o = 0
        self.assertEqual(s.findUnsortedSubarray(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = 0
        self.assertEqual(s.findUnsortedSubarray(i), o)

    def test_four(self):
        s = Solution()
        i = [8,9,1,2,3]
        o = 5
        self.assertEqual(s.findUnsortedSubarray(i), o)

    def test_five(self):
        s = Solution()
        i = [1,1,1,2,3,3,3]
        o = 0
        self.assertEqual(s.findUnsortedSubarray(i), o)

    def test_six(self):
        s = Solution()
        i = [1,3,2,2,2]
        o = 4
        self.assertEqual(s.findUnsortedSubarray(i), o)

    def test_seven(self):
        s = Solution()
        i = [3,2,3,2,4]
        o = 4
        self.assertEqual(s.findUnsortedSubarray(i), o)

    def test_eight(self):
        s = Solution()
        i = [1,3,5,2,4]
        o = 4
        self.assertEqual(s.findUnsortedSubarray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)