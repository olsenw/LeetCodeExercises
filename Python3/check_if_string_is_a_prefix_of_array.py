# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an array of strings words, determine whether s is a
    prefix string of words.

    A string s is a prefix string of words if s can be made by concatenating the
    first k strings in words for some positive k no larger than words.length.

    Return true if s is a prefix string of words, or false otherwise.
    '''
    # wrong allows partial matches
    def isPrefixString_wrong(self, s: str, words: List[str]) -> bool:
        prefix = ''.join(words)
        i,j = 0,0
        while i < len(s) and j < len(prefix):
            if s[i] != prefix[j]:
                return False
            i += 1
            j += 1
        return i == len(s)

    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i,j,k = 0,0,0
        while i < len(s) and j < len(words):
            if s[i] != words[j][k]:
                return False
            i += 1
            k += 1
            if k == len(words[j]):
                j += 1
                k = 0
        return i == len(s) and k == 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "iloveleetcode"
        j = ["i","love","leetcode","apples"]
        o = True
        self.assertEqual(s.isPrefixString(i,j), o)

    def test_two(self):
        s = Solution()
        i = "iloveleetcode"
        j = ["apples","i","love","leetcode"]
        o = False
        self.assertEqual(s.isPrefixString(i,j), o)

    def test_three(self):
        s = Solution()
        i = "a"
        j = ["aa","aaaa","banana"]
        o = False
        self.assertEqual(s.isPrefixString(i,j), o)

    def test_four(self):
        s = Solution()
        i = "ccccccccc"
        j = ["c","cc"]
        o = False
        self.assertEqual(s.isPrefixString(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)