# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n and a 2D integer array queries of
    size q, where queries[i] = [li, ri, ki, vi].

    For each query, apply the following operations in order:
    * Set idx = li
    * While idx <= ri:
        * Update: nums[idx] = (nums[idx] * vi) % (10^9 + 7)
        * Set idx += ki.
    
    Return the bitwise XOR of all elements in nums after processing all queries.
    '''
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        m = 10**9 + 7
        for l,r,k,v in queries:
            for i in range(l, r+1, k):
                nums[i] = (nums[i] * v) % m
        answer = nums[0]
        for i in range(1, len(nums)):
            answer ^= nums[i]
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