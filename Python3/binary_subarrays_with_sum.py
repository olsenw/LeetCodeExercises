# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from collections import defaultdict
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary array nums and an integer goal, return the number of
    non-empty subarrays with a sum goal.

    A subarray is a contiguous part of the array.
    '''
    def numSubarraysWithSum_brute(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        answer = 0
        prefix = [0] + list(accumulate(nums))
        for i in range(n):
            for j in range(i, n):
                if prefix[j+1] - prefix[i] == goal:
                    answer += 1
        return answer

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix = defaultdict(list)
        s = 0
        for i,j in enumerate(nums):
            s += j
            prefix[s].append(i)
        s = 0
        answer = 0
        for i in range(n):
            if len(prefix[s+goal]) > 0:
                answer += len(prefix[s+goal]) - bisect.bisect_left(prefix[s+goal],i)
            s += nums[i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,0,1,0,1]
        j = 2
        o = 4
        self.assertEqual(s.numSubarraysWithSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [0,0,0,0,0]
        j = 0
        o = 15
        self.assertEqual(s.numSubarraysWithSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)