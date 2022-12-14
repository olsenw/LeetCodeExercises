# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A professional robber is planning to rob houses along a street. Each house
    has a certain amount of money stashed, the only constraint preventing the
    robber from robbing all the houses is that adjacent houses have connected
    security systems that will contact the police if two adjacent houses are
    broken into on the same night.

    Given an integer array nums representing the amount of money in each house,
    return the maximum amount of money that the robber can steal without
    alerting the police.
    '''
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(house):
            # base case - no more houses
            if house >= len(nums):
                return 0
            # rob this house
            a = nums[house] + dp(house+2)
            # skip this house
            b = dp(house+1)
            # what made more money
            return max(a,b)
        return dp(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,1]
        o = 4
        self.assertEqual(s.rob(i), o)

    def test_two(self):
        s = Solution()
        i = [2,7,9,3,1]
        o = 12
        self.assertEqual(s.rob(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)