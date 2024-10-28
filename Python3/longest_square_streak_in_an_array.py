# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. A subsequence of nums is called a square streak
    if:
    * The length of the subsequence is at least 2, and
    * after sorting the subsequence, each element (except the first element) is
      the square of the previous number.
    
    Return the length of the longest square streak in nums, or return -1 if
    there is no square streak.

    A subsequence is an array that can be derived from another array by deleting
    some or no elements without changing the order of the remaining elements.
    '''
    # hints are really helpful
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        @cache
        def dp(i:int):
            if i * i in nums:
                return 1 + dp(i * i)
            return 0
        answer = max(1 + dp(i) for i in nums)
        return -1 if answer == 1 else answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,3,6,16,8,2]
        o = 3
        self.assertEqual(s.longestSquareStreak(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,5,6,7]
        o = -1
        self.assertEqual(s.longestSquareStreak(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)