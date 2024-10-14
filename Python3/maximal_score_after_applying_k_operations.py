# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums and an integer k. The starting score is
    0.

    In one operation:
    1. choose an index i such that 0 <= i < nums.length,
    2. increase the score by nums[i], and
    3. replace nums[i] with ceil(nums[i] / 3)

    Return the maximum possible score that can be obtained after applying
    exactly k operations.

    The ceiling function ceil(val) is the least integer greater than or equal to
    val.
    '''
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        score = 0
        for _ in range(k):
            score -= heapq.heapreplace(nums, math.floor(nums[0] / 3))
        return score

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,10,10,10,10], 5
        o = 50
        self.assertEqual(s.maxKelements(*i), o)

    def test_two(self):
        s = Solution()
        i = [1,10,3,3,3], 3
        o = 17
        self.assertEqual(s.maxKelements(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)