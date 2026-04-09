# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from math import ceil, sqrt
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n and a 2D integer array queries of
    size q, where queries[i] = [li, ri, ki, vi].

    For each query, apply the following operations in order:
    * Set idx = li.
    * While idx <= ri.
        * Update: nums[idx] = (nums[idx] * vi) % (10^9 + 7).
        * Set idx += ki.
    
    Return the bitwise XOR of all elements in nums after processing all queries.
    '''
    # based on editorial by LeetCode
    # https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/editorial/?envType=daily-question&envId=2026-04-09
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9+7
        n = len(nums)
        # determine the size where k steps is small
        T = int(n**0.5)
        # divide the queries into the k steps
        groups = [[] for _ in range(T)]
        for l,r,k,v in queries:
            # would impact a lot positions
            if k < T:
                groups[k].append((l,r,v))
            # "few" positions impacted, compute directly
            else:
                for i in range(l, r+1, k):
                    nums[i] = nums[i] * v % mod
        # multiplication for condensed queries
        dif = [1] * (n + T)
        for k in range(1, T):
            # nothing in this group of queries
            if not groups[k]:
                continue
            # reset dif array
            dif[:] = [1] * len(dif)
            for l,r,v in groups[k]:
                # add difference to l
                dif[l] = dif[l] * v % mod
                # last index impacted by query
                R = ((r-l) // k + 1) * k + l
                # inverse of v (undo the difference at R)
                dif[R] = dif[R] * pow(v, mod-2, mod) % mod
            
            # apply the multiplication to each element
            for i in range(k, n):
                dif[i] = dif[i] * dif[i - k] % mod
            for i in range(n):
                nums[i] = nums[i] * dif[i] % mod
        
        # calculate final answer
        answer = 0
        for x in nums:
            answer ^= x
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,1]
        j = [[0,2,1,4]]
        o = 4
        self.assertEqual(s.xorAfterQueries(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,3,1,5,4]
        j = [[1,4,2,3],[0,2,1,2]]
        o = 31
        self.assertEqual(s.xorAfterQueries(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)