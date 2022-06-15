# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from functools import cache
class Solution:
    '''
    Given an array of words where each word consists of lowercase
    English letters.

    wordA is a predecessor of wordB if and only if inserting exactly one
    letter anywhere in wordA without changing the order of the other
    characters to make it equal to wordB. (For example "abc" is a 
    predecessor of "abac" while "cba" is not a predecessor of "bcad".)

    A word chain is a sequence of words [word1, word2, ..., wordk] with
    k >= 1, where word1 is a predecessor of word2, word2 is a
    predecessor of word3, and so on. A single word is trivially a word
    chain with k == 1.

    Return the length of the longest possible word chain with words
    chosen from the given list of words.
    '''
    # works, slower than I like
    def longestStrChain(self, words: List[str]) -> int:
        h = dict()
        for w in words:
            if len(w) in h:
                h[len(w)].append(w)
            else:
                h[len(w)] = [w]
        @cache
        def dp(s):
            if len(s) not in h:
                return 0
            if s not in h[len(s)]:
                return 0
            if len(s) == 1:
                return 1
            m = 0
            for i in range(len(s)):
                m = max(m, dp(s[:i] + s[i+1:]))
            return m + 1
        return max(max(dp(s) for s in v) for v in h.values())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["a","b","ba","bca","bda","bdca"]
        o = 4
        self.assertEqual(s.longestStrChain(i), o)

    def test_two(self):
        s = Solution()
        i = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
        o = 5
        self.assertEqual(s.longestStrChain(i), o)

    def test_three(self):
        s = Solution()
        i = ["abcd","dbqca"]
        o = 1
        self.assertEqual(s.longestStrChain(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)