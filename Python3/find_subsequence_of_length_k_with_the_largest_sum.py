# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k. Find the subsequence of nums
    of length k that has the largest sum.

    Return any such subsequence as an integer array of length k.

    A subsequence is an array that can be derived from another array by deleting
    some or no elements without changing the order of the remaining elements.
    '''
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i,j in enumerate(nums):
            if len(heap) < k:
                heapq.heappush(heap, (j,i))
            else:
                heapq.heappushpop(heap, (j,i))
        return [i for i,_ in sorted(heap, key=lambda x: x[1])]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,3,3], 2
        o = [3,3]
        self.assertEqual(s.maxSubsequence(*i), o)

    def test_two(self):
        s = Solution()
        i = [-1,-2,3,4], 3
        o = [-1,3,4]
        self.assertEqual(s.maxSubsequence(*i), o)

    def test_three(self):
        s = Solution()
        i = [3,4,3,3], 2
        o = [4,3]
        self.assertEqual(s.maxSubsequence(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)