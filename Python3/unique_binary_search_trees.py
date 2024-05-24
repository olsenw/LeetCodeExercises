# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, return the number of structurally unique BST's (binary
    search trees) which has exactly n nodes of unique values from 1 to n.
    '''
    def numTrees_wrong(self, n: int) -> int:
        answer = 0
        @cache
        def dp(x):
            if x < 3:
                return x
            if x == 3:
                return 5
            l = dp(x-1)
            r = dp(x-1)
            return x * l * r
        return dp(n)

    # based on solution by liaison
    # https://leetcode.com/problems/unique-binary-search-trees/
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        o = 5
        self.assertEqual(s.numTrees(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.numTrees(i), o)

    def test_three(self):
        s = Solution()
        i = 4
        o = 14
        self.assertEqual(s.numTrees(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)