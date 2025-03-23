# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of size n. For each index i where 0 <= i < n,
    define a subarray nums[start ... i] where start = max(0, i - nums[i]).

    Return the total sum of all elements from the subarray defined for each
    index in the array.
    '''
    def subarraySum_brute(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            answer += sum(nums[start:i+1])
        return answer

    def subarraySum_oneline(self, nums: List[int]) -> int:
        return sum(sum(nums[max(0,i-nums[i]):i+1]) for i in range(len(nums)))

    def subarraySum(self, nums: List[int]) -> int:
        answer = 0
        nums = [0] + nums
        for i in range(1, len(nums)):
            start = max(0, i - 1 - nums[i])
            nums[i] += nums[i-1]
            answer += nums[i] - nums[start]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,1]
        o = 11
        self.assertEqual(s.subarraySum(i), o)

    def test_two(self):
        s = Solution()
        i = [3,1,1,2]
        o = 13
        self.assertEqual(s.subarraySum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)