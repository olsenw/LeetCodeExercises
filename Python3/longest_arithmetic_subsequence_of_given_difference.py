# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array arr and an integer difference, return the length of
    the longest subsequence in arr which is an arithmetic sequence such that the
    difference between adjacent elements in the subsequence equals difference.

    A subsequence is a sequence is a sequence that can be derived from arr by
    deleting some or no elements without changing the order of the remaining
    elements.
    '''
    # hints are pretty good
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        m = 0
        dp = dict()
        for i in arr:
            if i - difference in dp:
                dp[i] = 1 + dp[i - difference]
            else:
                dp[i] = 1
            m = max(m, dp[i])
        return m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        j = 1
        o = 4
        self.assertEqual(s.longestSubsequence(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,3,5,7]
        j = 1
        o = 1
        self.assertEqual(s.longestSubsequence(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,5,7,8,5,3,4,2,1]
        j = -2
        o = 4
        self.assertEqual(s.longestSubsequence(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)