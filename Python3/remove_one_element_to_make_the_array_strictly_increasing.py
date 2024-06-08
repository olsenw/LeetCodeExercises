# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums, return true if it can be made strictly
    increasing after removing exactly one element, or false otherwise. If the
    array is already strictly increasing, return True.

    The array nums is strictly increasing if nums[i - 1] < nums[i] for each
    index (1 <= i < nums.length).
    '''
    def canBeIncreasing_fails(self, nums: List[int]) -> bool:
        c = False
        i = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                i += 1
                continue
            if c:
                return False
            c = True
            if i+2 >= len(nums):
                return True
            if nums[i] >= nums[i+2]:
                return False
            i = i + 2
        return True

    def canBeIncreasing_fail(self, nums: List[int]) -> bool:
        def test(nums):
            for i in range(len(nums) - 1):
                if nums[i] >= nums[i+1]:
                    return i
            return len(nums)
        t = test(nums)
        if t == len(nums):
            return True
        if test(nums[:t] + nums[t+1:]) == len(nums) - 1:
            return True
        return False

    def canBeIncreasing(self, nums: List[int]) -> bool:
        def first(nums):
            if nums[0] >= nums[1]:
                return 0
            i = 1
            while i < len(nums) - 1:
                if nums[i-1] < nums[i] < nums[i+1]:
                    i += 1
                    continue
                if nums[i-1] < nums[i+1]:
                    return i
                return i + 1
            return len(nums)
        def second(nums):
            for i in range(len(nums) - 1):
                if nums[i] < nums[i+1]:
                    continue
                return False
            return True
        t = first(nums)
        if t == len(nums):
            return True
        return second(nums[:t] + nums[t+1:])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,10,5,7]
        o = True
        self.assertEqual(s.canBeIncreasing(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,1,2]
        o = False
        self.assertEqual(s.canBeIncreasing(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1]
        o = False
        self.assertEqual(s.canBeIncreasing(i), o)

    def test_four(self):
        s = Solution()
        i = [3,1,2]
        o = True
        self.assertEqual(s.canBeIncreasing(i), o)

    def test_five(self):
        s = Solution()
        i = [2,3,1]
        o = True
        self.assertEqual(s.canBeIncreasing(i), o)

    def test_six(self):
        s = Solution()
        i = [2,1]
        o = True
        self.assertEqual(s.canBeIncreasing(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)