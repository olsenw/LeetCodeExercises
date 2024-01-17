# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings patterns and a string word, return the number of
    strings in patterns that exist as a substring in word.

    A substring is a contiguous sequence of characters within a string.
    '''
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)
    
    # could also solve this with a trie or regex

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["a","abc","bc","d"]
        j = "abc"
        o = 3
        self.assertEqual(s.numOfStrings(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["a","b","c"]
        j = "aaaaabbbbb"
        o = 2
        self.assertEqual(s.numOfStrings(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["a","a","a"]
        j = "ab"
        o = 3
        self.assertEqual(s.numOfStrings(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)