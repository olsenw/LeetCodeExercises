# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from bisect import bisect_left
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a list of strings of the same length words and a string target.

    Form target using the given words under the following rules:
    * target should be formed from left to right.
    * To form the ith character (0-indexed) of target, choose the kth character
      of the jth sring in words if target[i] = words[j][k].
    * Once the kth character of the jth string in words is used it is no longer
      possible to use the xth character of any string in words where x <= k. In
      other words, all characters to the left of or at index k become unusable
      for every string.
    * Repeat the process until the target string is formed. 

    Notice that is is possible to use multiple character from the same string in
    words provided the conditions above are met.

    Return the number of ways to form target from words. Since the answer may be
    too large, return it modulo 10^9 + 7.
    '''
    # seems correct times out on test case 73/89
    def numWays_timeout(self, words: List[str], target: str) -> int:
        m = 10**9 + 7
        # i is index in target
        # j is index in words[x]
        @cache
        def dp(i:int, j:int) -> int:
            if i == len(target) - 1:
                return sum(sum(1 for w in words if w[k] == target[i]) for k in range(j, len(words[0])))
            if j == len(words[0]) - 1:
                return 0
            answer = 0
            for k in range(j, len(words[0])):
                for w in words:
                    if w[k] == target[i]:
                        answer = ((answer % m) + (dp(i+1,k+1) % m)) % m
            return answer
        return dp(0,0)

    # leetcode bottom up solution
    # https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/editorial/
    # dp is similar to what I was doing but much smarter way of tracking valid
    # indices and counting
    def numWays_leetcode(self, words: List[str], target: str) -> int:
        alphabet = 26
        mod = 1000000007
        m = len(target)
        k = len(words[0])
        cnt = [[0] * k for _ in range(alphabet)]
        for j in range(k):
            for word in words:
                cnt[ord(word[j]) - ord('a')][j] += 1
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(m + 1):
            for j in range(k):
                if i < m:
                    dp[i + 1][j + 1] += (cnt[ord(target[i]) - ord('a')][j]
                                         * dp[i][j])
                    dp[i + 1][j + 1] %= mod
                dp[i][j + 1] += dp[i][j]
                dp[i][j + 1] %= mod
        return dp[m][k]

    # seems correct times out on test case 74/89
    def numWays_timeout2(self, words: List[str], target: str) -> int:
        m = 10**9 + 7
        indexes = [{i:[] for i in "abcdefghijklmnopqrstuvwxyz"} for w in words]
        for i,w in enumerate(words):
            for j,c in enumerate(w):
                indexes[i][c].append(j)
        @cache
        def dp(i:int, j:int) -> int:
            if i == len(target) - 1:
                return sum(len(indexes[w][target[i]]) - bisect_left(indexes[w][target[i]], j) for w in range(len(words)))
            if j == len(words[0]) - 1:
                return 0
            answer = 0
            for w in range(len(words)):
                for k in range(
                    bisect_left(indexes[w][target[i]], j),
                    len(indexes[w][target[i]])
                ):
                    answer = ((answer % m) + (dp(i+1,indexes[w][target[i]][k]+1) % m)) % m
            return answer
        return dp(0,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["acca","bbbb","caca"]
        j = "aba"
        o = 6
        self.assertEqual(s.numWays(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["abba","baab"]
        j = "bab"
        o = 4
        self.assertEqual(s.numWays(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["aa","cc"]
        j = "a"
        o = 2
        self.assertEqual(s.numWays(i,j), o)

    def test_four(self):
        s = Solution()
        i = ["egeggk","gajeke","jigija","ijkcik","jbhebg","gfffdi","fkdgdi"]
        j = "ia"
        o = 5
        self.assertEqual(s.numWays(i,j), o)

    def test_five(self):
        s = Solution()
        i = ["gajeke","jigija","ijkcik"]
        j = "ia"
        o = 5
        self.assertEqual(s.numWays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)