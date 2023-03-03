# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an integer array nums sorted in ascending order (with distinct
    values).

    Prior to being passed to the function, nums is possibly rotated at an
    unknown pivot index k (1 <= k <= num.length) such that the resulting array
    is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
    (0-indexed).

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.

    Write an algorithm with O(log n) runtime complexity.
    '''
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # find pivot
        i,j,k = 0, n - 1, 0
        while i < j:
            k = (j - i) // 2 + i
            if nums[k] > nums[j]:
                i = k + 1
            else:
                j = k
        # find value
        if i == 0:
            i,j = 0, n - 1
        elif nums[i] <= target <= nums[n - 1]:
            i,j = i, n - 1
        else:
            i,j = 0, i - 1
        while i <= j:
            k = (j - i) // 2 + i
            if nums[k] == target:
                return k
            elif nums[k] < target:
                i = k + 1
            else:
                j = k - 1
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,5,6,7,0,1,2]
        j = 0
        o = 4
        self.assertEqual(s.search(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,5,6,7,0,1,2]
        j = 3
        o = -1
        self.assertEqual(s.search(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1]
        j = 1
        o = 0
        self.assertEqual(s.search(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1]
        j = 0
        o = -1
        self.assertEqual(s.search(i,j), o)

    def test_five(self):
        s = Solution()
        i = [1,2,3,4]
        j = 0
        o = -1
        self.assertEqual(s.search(i,j), o)

    def test_six(self):
        s = Solution()
        i = [3,1]
        j = 1
        o = 1
        self.assertEqual(s.search(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)