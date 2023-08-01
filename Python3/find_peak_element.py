# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A peak element is an element that is strictly greater than its neighbors.

    Given a 0-indexed integer array nums, find a peak element and return its
    index. If the array contains multiple peaks, return the index to any of the
    peaks.

    Consider nums[-1] = nums[n] = -infinity. In other words, an element is
    always greater than a neighbor outside of the array.

    Write an algorithm that runs in O(log n) time.
    '''
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n-1
        i,j = 0, n-1
        while i <= j:
            k = (i + j) // 2
            if nums[k-1] < nums[k] > nums[k+1]:
                return k
            if nums[k-1] > nums[k]:
                j = k - 1
            else:
                i = k + 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,1]
        o = 2
        self.assertEqual(s.findPeakElement(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,1,3,5,6,4]
        o = 5
        self.assertEqual(s.findPeakElement(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)