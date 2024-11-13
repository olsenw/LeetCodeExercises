# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums of size n and two integers lower and
    upper, return the number of fair pairs.

    A pair (i,j) is fair if:
    * 0 <= i < j < n, and
    * lower <= nums[i] + nums[j] <= upper
    '''
    def countFairPairs_fails(self, nums: List[int], lower: int, upper: int) -> int:
        answer = 0
        nums.sort()
        for i in range(1,len(nums)):
            j = bisect.bisect(nums, min(0, lower - nums[i]), 0, i)
            if lower <= nums[i] + nums[j] <= upper:
                answer += i - j
        return answer

    # based on leetcode solution
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        answer = 0
        nums.sort()
        for i in range(len(nums)):
            l = bisect.bisect_left(nums, lower - nums[i], i+1)
            u = bisect.bisect(nums, upper - nums[i], i+1)
            answer += u - l
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,7,4,4,5]
        j = 3
        k = 6
        o = 6
        self.assertEqual(s.countFairPairs(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,7,9,2,5]
        j = 11
        k = 11
        o = 1
        self.assertEqual(s.countFairPairs(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [0,0,0,0,0,0]
        j = 0
        k = 0
        o = 15
        self.assertEqual(s.countFairPairs(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)