# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer target.

    Build an expression out of nums by adding one of the symbols '+' and '-'
    before each integer in nums and then concatenate all the integers.

    Return the number of different expressions that can be built that evaluate
    to target.
    '''
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(index, total):
            if index == len(nums):
                return target == total
            return dfs(index + 1, total + nums[index]) + dfs(index + 1, total - nums[index])
        return dfs(0,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,1,1,1]
        j = 3
        o = 5
        self.assertEqual(s.findTargetSumWays(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1]
        j = 1
        o = 1
        self.assertEqual(s.findTargetSumWays(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        j = 4
        o = 125970
        self.assertEqual(s.findTargetSumWays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)