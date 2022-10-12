# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums, return the largest perimeter of a triangle with
    a non-zero area, formed from three of these lengths. If it is impossible to
    form any triangle of a non-zero area, return 0.
    '''
    def largestPerimeter_slow_zip(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        p = 0
        for c,b,a in zip(nums[:-2], nums[1:-1], nums[2:]):
            if a + b > c:
                p = max(p, c + b + a)
        return p

    def largestPerimeter_slow_index(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        p = 0
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] + nums[i+1]:
                p = max(p, nums[i-1] + nums[i] + nums[i+1])
        return p

    # based off of sample submission for 207 ms
    # https://leetcode.com/submissions/api/detail/1018/python3/207
    # do not get the same performance in leetcode...
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i, j, k = 0, 1, 2
        while k < len(nums) - 1 and nums[i] >= nums[j] + nums[k]:
            i = j
            j = k
            k += 1
        if nums[i] >= nums[j] + nums[k]:
            return 0
        return nums[i] + nums[j] + nums[k]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,2]
        o = 5
        self.assertEqual(s.largestPerimeter(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,1]
        o = 0
        self.assertEqual(s.largestPerimeter(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)