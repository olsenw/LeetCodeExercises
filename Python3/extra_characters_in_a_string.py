# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Trie:
    def __init__(self, words=[]) -> None:
        self.trie = [dict(), False]
        for w in words:
            self.add(w)
    
    def add(self, word) -> None:
        curr = self.trie
        for w in word:
            if w not in curr[0]:
                curr[0][w] = [dict(), False]
            curr = curr[0][w]
        curr[1] = True

    def contains(self, word) -> bool:
        curr = self.trie
        for w in word:
            if w not in curr[0]:
                return False
            curr = curr[0][w]
        return curr[1]

class Solution:
    '''
    Given a 0-indexed string s and a dictionary of words dictionary. Break
    string s into one or more non-overlapping substrings such that each
    substring is present in dictionary. There may be some extra characters in s
    which are not present in any of the substrings.

    Return the minimum number of extra characters left over if the string s is
    broken up optimally.
    '''
    # correct idea, failed implementation
    def minExtraChar_wrong(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        trie = Trie(dictionary)
        dp = [i for i in range(0,n+1)]
        if trie.contains(s[0]):
            dp[1] = 0
        for i in range(1, n):
            for j in range(i+1):
                if trie.contains(s[j:i+1]):
                    dp[i] = min(dp[i], dp[j-1])
                else:
                    dp[i] = min(dp[i], 1 + dp[j-1])
        return dp[-1]

    # some help from editorial on direction
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        trie = Trie(dictionary)
        @cache
        def dp(i):
            if i == n:
                return 0
            # count the current character as left over
            answer = dp(i+1) + 1
            for j in range(i, n):
                if trie.contains(s[i:j+1]):
                    answer = min(answer, dp(j+1))
            return answer
        return dp(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "leetscode"
        j = ["leet","code","leetcode"]
        o = 1
        self.assertEqual(s.minExtraChar(i,j), o)

    def test_two(self):
        s = Solution()
        i = "sayhelloworld"
        j = ["hello","world"]
        o = 3
        self.assertEqual(s.minExtraChar(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)