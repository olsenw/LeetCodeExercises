# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n and a 2D array queries where
    queries[i] = [li, ri, vali].

    Each queries[i] represents the following action on num:
    * Decrement the value at each index in the range [li, ri] in nums by at most
      vali.
    * The amount by which each value is decremented can be chosen independently
      for each index.
    
    A Zero Array is an array with all elements equal to 0.

    Return the minimum possible non-negative value of k, such that after
    processing the first k queries in sequence nums becomes a Zero Array. If no
    such k exists, return -1.
    '''
    def minZeroArray_brute(self, nums: List[int], queries: List[List[int]]) -> int:
        answer = 0
        if all(n == 0 for n in nums):
            return answer
        for i,j,k in queries:
            answer += 1
            for a in range(i,j+1):
                nums[a] = max(0, nums[a] - k)
            if all(n == 0 for n in nums):
                return answer
        return -1

    # based on Leetcode line sweep solution
    # https://leetcode.com/problems/zero-array-transformation-ii/editorial/?envType=daily-question&envId=2025-03-13
    # pretty neat uses difference array to track future changes that will be
    # applied later, while dealing with the now.
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        s = 0
        answer = 0
        diff = [0] * (n+1)
        for i in range(n):
            while s + diff[i] < nums[i]:
                answer += 1
                if answer > len(queries):
                    return -1
                left, right, value = queries[answer-1]
                if right >= i:
                    diff[max(left,i)] += value
                    diff[right+1] -= value
            s += diff[i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,0,2]
        j = [[0,2,1],[0,2,1],[1,1,3]]
        o = 2
        self.assertEqual(s.minZeroArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,3,2,1]
        j = [[1,3,2],[0,2,1]]
        o = -1
        self.assertEqual(s.minZeroArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)