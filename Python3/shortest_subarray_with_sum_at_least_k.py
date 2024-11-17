# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k, return the length of the
    shortest non-empty subarray of nums with a sum of at least k. If there is no
    such subarray, return -1.

    A subarray is a contiguous part of an array.
    '''
    # negative numbers break the shrink
    def shortestSubarray_fails(self, nums: List[int], k: int) -> int:
        answer = len(nums) + 1
        n = 0
        i = 0
        s = 0
        for j in range(len(nums)):
            s += nums[j]
            n += abs(nums[j])
            pass
            while s >= k or n > k:
                answer = min(answer, j - i + 1)
                s -= nums[i]
                n -= abs(nums[i])
                i += 1
        return -1 if answer == len(nums) + 1 else answer

    def shortestSubarray_brute(self, nums: List[int], k: int) -> int:
        answer = len(nums) + 1
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                if j - i + 1 >= answer:
                    break
                s += nums[j]
                if s >= k:
                    answer = min(answer, j - i + 1)
        return answer if answer != len(nums) + 1 else -1

    def shortestSubarray_fails2(self, nums: List[int], k: int) -> int:
        answer = len(nums) + 1
        i = 0
        s = 0
        n = 0
        m = 0
        for j in range(len(nums)):
            s += nums[j]
            n += abs(nums[j])
            if nums[j] < 0:
                k += abs(nums[j])
                m += abs(nums[j])
            pass
            while n >= k:
                if s >= k - m:
                    answer = min(answer, j - i + 1)
                s -= nums[i]
                n -= abs(nums[i])
                if nums[i] < 0:
                    k -= abs(nums[i])
                    m -= abs(nums[i])
                i += 1
        return -1 if answer == len(nums) + 1 else answer

    # based on leetcode min heap sliding editorial
    # https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/editorial/?envType=daily-question&envId=2024-11-17
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = len(nums) + 1
        s = 0
        h = []
        for i in range(n):
            s += nums[i]
            if s >= k:
                answer = min(answer, i + 1)
            while h and s - h[0][0] >= k:
                _,j = heapq.heappop(h)
                answer = min(answer, i - j)
            heapq.heappush(h, [s,i])
        return -1 if answer == len(nums) + 1 else answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1]
        j = 1
        o = 1
        self.assertEqual(s.shortestSubarray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        j = 4
        o = -1
        self.assertEqual(s.shortestSubarray(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2,-1,2]
        j = 3
        o = 3
        self.assertEqual(s.shortestSubarray(i,j), o)

    def test_four(self):
        s = Solution()
        i = [84,-37,32,40,95]
        j = 167
        o = 3
        self.assertEqual(s.shortestSubarray(i,j), o)

    def test_five(self):
        s = Solution()
        i = [-28,81,-20,28,-29]
        j = 89
        o = 3
        self.assertEqual(s.shortestSubarray(i,j), o)

    def test_six(self):
        s = Solution()
        i = [27,20,79,87,-36,78,76,72,50,-26]
        j = 453
        o = 9
        self.assertEqual(s.shortestSubarray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)