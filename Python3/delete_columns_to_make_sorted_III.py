# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of n strings strs, all of the same length.

    It is possible to delete any indices, by deleting all the characters in
    those indices for each string.

    Suppose that a set of deletion indices answer are chosen such that after
    deletions, the final array has every string (row) in lexicographic order.
    (ie (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]), and
    (strs[1][0] <= strs[1][1] <= ...<= strs[1][strs[1].length - 1]), and so on).
    Return the minimum possible value of answer.length.    
    '''
    # based on LeetCode editorial
    # https://leetcode.com/problems/delete-columns-to-make-sorted-iii/editorial/?envType=daily-question&envId=2025-12-22
    # idea is to use dp to track columns that can be kept
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n
        # work backwards
        for i in range(n-2,-1,-1):
            # compare columns at two indices
            for j in range(i+1, n):
                # going down all rows check if two selected columns are lexicographic
                if all(row[i] <= row[j] for row in strs):
                    # update to for best answer (can also assume all rows after j are good)
                    dp[i] = max(dp[i], 1 + dp[j])
        return n - max(dp)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["babca","bbazb"]
        o = 3
        self.assertEqual(s.minDeletionSize(i), o)

    def test_two(self):
        s = Solution()
        i = ["ghi","def","abc"]
        o = 0
        self.assertEqual(s.minDeletionSize(i), o)

    def test_three(self):
        s = Solution()
        i = ["edcba"]
        o = 4
        self.assertEqual(s.minDeletionSize(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)