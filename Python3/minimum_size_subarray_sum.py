# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers nums and a positive integer target,
    return the minimal length of a subarray whose sum is greater than or equal
    to target. If there is no such subarray, return 0 instead.
    '''
    # O(n^2) time
    def minSubArrayLen_tle(self, target: int, nums: List[int]) -> int:
        if nums[-1] >= target:
            return 1
        p = list(accumulate(nums, initial=0))
        if p[-1] < target:
            return 0
        answer = 10**6
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                if p[j] - p[i] >= target:
                    answer = min(answer, j - i)
                    break
        return answer
   
    # just flat wrong... order matters...
    def minSubArrayLen_wrong(self, target: int, nums: List[int]) -> int:
        if nums[-1] >= target:
            return 1
        p = list(accumulate(nums, initial=0))
        if p[-1] < target:
            return 0
        answer = 10**6
        i,j = 0, len(p) - 1
        while i < j:
            if p[j] - p[i] >= target:
                answer = min(answer, j - i)
            if nums[i] < nums[j-1]:
                i += 1
            else:
                j -= 1
        return answer

    def minSubArrayLen_search_wrong(self, target: int, nums: List[int]) -> int:
        if nums[-1] >= target:
            return 1
        p = list(accumulate(nums, initial=0))
        if p[-1] < target:
            return 0
        answer = 10**6
        for i in range(len(p) - 1, 0, -1):
            if p[i] - target < 0:
                continue
            j = bisect.bisect_left(p, p[i] - target, 0, i + 1)
            answer = min(answer, i - j)
            pass
        return answer

    # O(n) sliding window
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = 10**6
        s = 0
        i = 0
        for j in range(len(nums)):
            s += nums[j]
            while s >= target:
                answer = min(answer, j - i + 1)
                s -= nums[i]
                i += 1
        return answer if answer != 10**6 else 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 7
        j = [2,3,1,2,4,3]
        o = 2
        self.assertEqual(s.minSubArrayLen(i,j), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [1,4,4]
        o = 1
        self.assertEqual(s.minSubArrayLen(i,j), o)

    def test_three(self):
        s = Solution()
        i = 11
        j = [1,1,1,1,1,1,1,1]
        o = 0
        self.assertEqual(s.minSubArrayLen(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)