# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums. A player is initially positioned at the array's
    first index, and each element in the array represents the maximum jump
    length at that position.

    Return true if the player can reach the last index, or false otherwise.
    '''
    def canJump_slow(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        @cache
        def dp(index):
            if index >= len(nums) - 1:
                return True
            for i in range(index+1, index + nums[index] + 1):
                if dp(i):
                    return True
            return False
        return dp(0)

    def canJump(self, nums: List[int]) -> bool:
        j = 0
        for i in range(len(nums)):
            if j >= len(nums) - 1:
                return True
            if i > j:
                return False
            j = max(j, i + nums[i])
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,1,1,4]
        o = True
        self.assertEqual(s.canJump(i), o)

    def test_two(self):
        s = Solution()
        i = [3,2,1,0,4]
        o = False
        self.assertEqual(s.canJump(i), o)

    def test_three(self):
        s = Solution()
        i = [0]
        o = True
        self.assertEqual(s.canJump(i), o)

    def test_four(self):
        s = Solution()
        i = [2,0,0]
        o = True
        self.assertEqual(s.canJump(i), o)

    def test_five(self):
        s = Solution()
        i = [0,2,3]
        o = False
        self.assertEqual(s.canJump(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)