# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and a dictionary of strings wordDict, add spaces in s to
    construct a sentence where each word is a valid dictionary word. Return all
    such possible sentences in any order.

    Note that the same word in the dictionary may be reused multiple times in
    the segmentation.
    '''
    def wordBreak_wrong(self, s: str, wordDict: List[str]) -> List[str]:
        trie = [False, dict()]
        for w in wordDict:
            curr = trie
            for c in w:
                if c not in curr[1]:
                    curr[1][c] = [False, dict()]
                curr = curr[1][c]
            curr[0] = True
        @cache
        def dp(i:int) -> List[str]:
            if i == len(s):
                return [""]
            a = []
            curr = trie
            for j in range(i, len(s)):
                if s[j] in curr[1]:
                    if curr[0] == True:
                        pass
                        for w in dp(j):
                            a.append(s[i:j+1] + w)
                    curr = curr[1][s[j]]
                else:
                    break
            if curr[0] == True:
                pass
                for w in dp(j):
                    a.append(s[i:j+1] + w)
            return a
        return dp(0)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wd = set(wordDict)
        @cache
        def dp(i:int) -> List[str]:
            if i == n:
                return []
            a = []
            for j in range(i, n):
                if s[i:j+1] in wd:
                    if j+1 == n:
                        a.append([s[i:j+1]])
                    else:
                        for d in dp(j+1):
                            a.append([s[i:j+1]] + d)
            return a
        return [" ".join(d) for d in dp(0)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "catsanddog"
        j = ["cat","cats","and","sand","dog"]
        o = sorted(["cats and dog","cat sand dog"])
        self.assertEqual(sorted(s.wordBreak(i,j)), o)

    def test_two(self):
        s = Solution()
        i = "pineapplepenapple"
        j = ["apple","pen","applepen","pine","pineapple"]
        o = sorted(["pine apple pen apple","pineapple pen apple","pine applepen apple"])
        self.assertEqual(sorted(s.wordBreak(i,j)), o)

    def test_three(self):
        s = Solution()
        i = "catsandog"
        j = ["cats","dog","sand","and","cat"]
        o = []
        self.assertEqual(s.wordBreak(i,j), o)

    def test_four(self):
        s = Solution()
        i = "aa"
        j = ["a","aa"]
        o = ["a a","aa"]
        self.assertEqual(s.wordBreak(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)