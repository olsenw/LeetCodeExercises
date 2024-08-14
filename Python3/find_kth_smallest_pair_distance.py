# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The distance of a pair of integers a and b is defined as the absolute
    difference between a and b.

    Given an integer array nums and an integer k, return the kth smallest
    distance among all the pairs nums[i] and nums[j] where
    0 <= i < j < nums.length.
    '''
    # O(n^2 log k) time
    def smallestDistancePair_brute(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        h = []
        for i in range(n):
            for j in range(i+1, n):
                if len(h) < k:
                    heapq.heappush(h, -(nums[j] - nums[i]))
                else:
                    heapq.heappushpop(h, -(nums[j] - nums[i]))
        return -heapq.heappop(h)

    # based on sliding window editorial
    # https://leetcode.com/problems/find-k-th-smallest-pair-distance/editorial/?envType=daily-question&envId=2024-08-14
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        i,j = 0, nums[-1] - nums[0]
        while i < j:
            m = i + ((j - i) // 2)
            x,c = 0,0
            for y in range(n):
                while nums[y] - nums[x] > m:
                    x += 1
                c += y - x
            if c < k:
                i = m + 1
            else:
                j = m
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,1]
        j = 1
        o = 0
        self.assertEqual(s.smallestDistancePair(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1]
        j = 2
        o = 0
        self.assertEqual(s.smallestDistancePair(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,6,1]
        j = 3
        o = 5
        self.assertEqual(s.smallestDistancePair(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)