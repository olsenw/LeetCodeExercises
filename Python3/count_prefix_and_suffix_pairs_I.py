# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed string array words.

    Define a boolean function isPrefixAndSuffix that takes two strings, str1 and
    str2.
    * isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a
      suffix of str2, and false otherwise.
    
    Return an integer denoting the number of index pairs (i,j) such that i < j,
    and isPrefixAndSuffix(words[i], words[j]) is true.
    '''
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(words[j].startswith(words[i]) and words[j].endswith(words[i]) for i in range(len(words)) for j in range(i+1, len(words)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["a","aba","ababa","aa"]
        o = 4
        self.assertEqual(s.countPrefixSuffixPairs(i), o)

    def test_two(self):
        s = Solution()
        i = ["pa","papa","ma","mama"]
        o = 2
        self.assertEqual(s.countPrefixSuffixPairs(i), o)

    def test_three(self):
        s = Solution()
        i = ["abab","ab"]
        o = 0
        self.assertEqual(s.countPrefixSuffixPairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)