# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List
from bisect import bisect

class Solution:
    '''
    Given a string s and an array of strings words, return the number of
    words[i] that is a subsequence of s.

    A subsequence of a string is a new string generated from the
    original string with some characters (can be none) deleted without
    changing the relative order of the remaining characters.
    '''
    # time limit exceeded (6/52 test cases)
    def numMatchingSubseq_tle(self, s: str, words: List[str]) -> int:
        class Trie:
            def __init__(self):
                self.t = dict()
            def add(self, c):
                for k in self.t:
                    self.t[k].add(c)
                if c not in self.t:
                    self.t[c] = Trie()
            def check(self, w):
                t = self.t
                for c in w:
                    if c not in t:
                        return False
                    t = t[c].t
                return True
        trie = Trie()
        for c in s:
            trie.add(c)
        a = 0
        for w in words:
            if trie.check(w):
                a += 1
        return a

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        t = {chr(c):[] for c in range(ord('a'),ord('z')+1)}
        for i,c in enumerate(s):
            t[c].append(i)
        a = 0
        for w in words:
            last = -1
            for c in w:
                curr = bisect(t[c], last)
                if curr == len(t[c]):
                    break
                last = t[c][curr]
            else:
                a += 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcde"
        j = ["a","bb","acd","ace"]
        o = 3
        self.assertEqual(s.numMatchingSubseq(i,j), o)

    def test_two(self):
        s = Solution()
        i = "dsahjpjauf"
        j = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
        o = 2
        self.assertEqual(s.numMatchingSubseq(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)