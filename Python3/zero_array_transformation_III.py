# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n and a 2D array queries where
    queries[i] = [li, ri].

    Each queries[i] represents the following action on nums:
    * Decrement the value at each index in the range [li, ri] in nums by at most
      1.
    * The amount by which the value is decremented can be chosen independently
      for each index.
    
    A Zero Array is an array with all its elements equal to 0.

    Return the maximum number of elements that can be removed from queries, such
    that nums can still be converted to a zero array using the remaining
    queries. If it is not possible to convert nums to zero array return -1.
    '''
    def maxRemoval_fails(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        answer = 0
        queries.sort(key=lambda x: (x[0], -x[1]))
        q = 0
        h = []
        s = 0
        for i in range(n):
            while h and h[0] < i:
                s -= 1
                heapq.heappop(h)
            while s < nums[i] and q < len(queries) and queries[q][0] <= i:
                if queries[q][1] >= i:
                    heapq.heappush(h, queries[q][1])
                    s += 1
                else:
                    answer += 1
                q += 1
            if s < nums[i]:
                return -1
        return len(queries) - q + answer

    # based on LeetCode Editorial
    # https://leetcode.com/problems/zero-array-transformation-iii/editorial/?envType=daily-question&envId=2025-05-22
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        delta = [0] * (len(nums)+1)
        queries.sort()
        q = 0
        heap = []
        operations = 0
        for i,n in enumerate(nums):
            operations += delta[i]
            while q < len(queries) and queries[q][0] == i:
                heapq.heappush(heap, - queries[q][1])
                q += 1
            while operations < n and heap and -heap[0] >= i:
                operations += 1
                delta[-heapq.heappop(heap) + 1] -= 1
            if operations < n:
                return -1
        return len(heap)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,0,2]
        j = [[0,2],[0,2],[1,1]]
        o = 1
        self.assertEqual(s.maxRemoval(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1]
        j = [[1,3],[0,2],[1,3],[1,2]]
        o = 2
        self.assertEqual(s.maxRemoval(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4]
        j = [[0,3]]
        o = -1
        self.assertEqual(s.maxRemoval(i,j), o)

    def test_four(self):
        s = Solution()
        i = [0,0,1,1,0]
        j = [[3,4],[0,2],[2,3]]
        o = 2
        self.assertEqual(s.maxRemoval(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)