# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, return the number of distinct non-empty subsequences of s.
    Since the answer may be very large, return it modulo 10^9 + 7.
    '''
    # based on leetcode solution
    # https://leetcode.com/problems/distinct-subsequences-ii/editorial/?envType=daily-question&envId=2026-09-07
    def distinctSubseqII(self, s: str) -> int:
        # dynamic programming
        # unique subsequences ending with letter at index in s
        dp = [1]
        last = {}
        for i,x in enumerate(s):
            # includes all unique subsequences to this point, and all those subsequences with an additional letter
            dp.append(dp[-1] * 2)
            # check if double counting subsequences by using a recurring letter
            if x in last:
                # remove duplicate subsequences
                dp[-1] -= dp[last[x]]
            # record last index a character was encountered
            last[x] = i
        # remove the empty index count
        return (dp[-1] - 1) % (10**9 + 7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        o = 7
        self.assertEqual(s.distinctSubseqII(i), o)

    def test_two(self):
        s = Solution()
        i = "aba"
        o = 6
        self.assertEqual(s.distinctSubseqII(i), o)

    def test_three(self):
        s = Solution()
        i = "aaa"
        o = 3
        self.assertEqual(s.distinctSubseqII(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)