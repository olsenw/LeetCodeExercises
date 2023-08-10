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

    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
    in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted array nums of unique elements, return the minimum element
    of this array.

    Write an algorithm that runs in O(log n) time.
    '''
    # O(n) time not O(log n)
    # easy though
    def findMin_invalid(self, nums: List[int]) -> int:
        return min (nums)

    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        i,j = 0,len(nums) - 1
        while i < j:
            k = i + (j - i) // 2
            if nums[k] < nums[j]:
                j = k
            else:
                i = k + 1
        return nums[i]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,4,5,1,2]
        o = 1
        self.assertEqual(s.findMin(i), o)

    def test_two(self):
        s = Solution()
        i = [4,5,6,7,0,1,2]
        o = 0
        self.assertEqual(s.findMin(i), o)

    def test_three(self):
        s = Solution()
        i = [11,13,15,17]
        o = 11
        self.assertEqual(s.findMin(i), o)

    def test_four(self):
        s = Solution()
        i = [0,1,2,3,4,5,6,7,8,9]
        o = 0
        for _ in range(len(i) + 1):
            self.assertEqual(s.findMin(i), o)
            i = [i[-1]] + i[:-1]

if __name__ == '__main__':
    unittest.main(verbosity=2)