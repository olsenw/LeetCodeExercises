# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and a positive integer k.

    A subsequence sub of nums with length x is called valid if it satisfies:
    * (sub[0]+sub[1])%k == (sub[1]+sub[2])%k + ... + (sub[x-2]+sub[x-1])%k.

    Return the length of the longest valid subsequence of nums.
    '''
    # based on LeetCode Editorial
    # https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/editorial/?envType=daily-question&envId=2025-07-17
    def maximumLength(self, nums: List[int], k: int) -> int:
        # maximum length of subsequence ending values i % k and j % k
        dp = [[0] * k for _ in range(k)]
        answer = 0
        for n in nums:
            n %= k
            for p in range(k):
                dp[p][n] = dp[n][p] + 1
                answer = max(answer, dp[p][n])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        j = 2
        o = 5
        self.assertEqual(s.maximumLength(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,4,2,3,1,4]
        j = 3
        o = 4
        self.assertEqual(s.maximumLength(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)