# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Suppose an array of length n sorted in ascending order is rotated between 1
    and n times.

    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 times
    results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums that may contain duplicates, return the
    minimum element of this array.

    Decrease the overall operation steps as much as possible.
    '''
    # O(n) not the best...
    def findMin_invalid(self, nums: List[int]) -> int:
        return min(nums)

    # based on answer by eunice
    # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/solutions/8244875/solution-by-la_castille-zqoe/?envType=daily-question&envId=2026-05-16
    def findMin(self, nums: List[int]) -> int:
        def divide(left:int, right:int) -> int:
            # base case only element is the minimum element
            if left == right:
                return nums[left]
            # because the subarray is already sorted, nums[left] is minimum
            if nums[left] < nums[right]:
                return nums[left]
            # segment has a rotation or duplicates at ends
            mid = (left + right) // 2
            # return the minimum of two subarrays
            return min(divide(left,mid), divide(mid+1,right))
        return divide(0, len(nums) - 1)

    '''
    The big take away by adding duplicates is that best time worst case is
    linear, because each element needs to be checked
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,5]
        o = 1
        self.assertEqual(s.findMin(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2,2,0,1]
        o = 0
        self.assertEqual(s.findMin(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)