# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n and a 2D array queries, where
    queries[i] = [li, ri].

    For each queries[i]:
    * Select a subset of indices within the range [li,ri] in nums.
    * Decrement the values at the selected indices by 1.

    A Zero Array is an array where all elements are equal to 0.

    Return true if it is possible to transform nums into a Zero Array after
    processing all the queries sequentially, otherwise return false.
    '''
    # slow O(nlogn + m)
    def isZeroArray_passes(self, nums: List[int], queries: List[List[int]]) -> bool:
        queries.sort(key = lambda x:(x[0],-x[1]))
        q = 0
        s = []
        for i,j in enumerate(nums):
            while s and s[0] < i:
                heapq.heappop(s)
            while q < len(queries) and queries[q][0] == i:
                heapq.heappush(s, queries[q][1])
                q += 1
            if j > len(s):
                return False
        return True

    # based on other Leetcode solutions
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        d = [0] * (n+1)
        for i,j in queries:
            d[i] += 1
            d[j+1] -= 1
        s = 0
        for i in range(n):
            s += d[i]
            if nums[i] > s:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,0,1]
        j = [[0,2]]
        o = True
        self.assertEqual(s.isZeroArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,3,2,1]
        j = [[1,3],[0,2]]
        o = False
        self.assertEqual(s.isZeroArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)