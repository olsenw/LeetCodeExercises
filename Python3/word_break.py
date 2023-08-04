# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and a dictionary of strings wordDict, return true if s can
    be segmented into a space separated sequence of one or more dictionary
    words.

    Note that the same word in the dictionary may be reused multiple times in
    the segmentation.
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        trie = [dict(), False]
        for word in wordDict:
            curr = trie
            for w in word:
                if w not in curr[0]:
                    curr[0][w] = [dict(), False]
                curr = curr[0][w]
            curr[1] = True
        @cache
        def dp(index) -> bool:
            if index == n:
                return True
            valid = False
            curr = trie
            while index < n:
                if s[index] in curr[0]:
                    curr = curr[0][s[index]]
                else:
                    break
                if curr[1]:
                    valid = valid or dp(index+1)
                index += 1
            return valid
        return dp(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "leetcode"
        j = ["leet","code"]
        o = True
        self.assertEqual(s.wordBreak(i,j), o)

    def test_two(self):
        s = Solution()
        i = "applepenapple"
        j = ["apple","pen"]
        o = True
        self.assertEqual(s.wordBreak(i,j), o)

    def test_three(self):
        s = Solution()
        i = "catsandog"
        j = ["cats","dog","sand","and","cat"]
        o = False
        self.assertEqual(s.wordBreak(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)