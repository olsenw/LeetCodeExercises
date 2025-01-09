# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings words and a string pref.

    Return the number of strings in words that contain pref as a prefix.

    A prefix of a string s is any leading contiguous substring of s.
    '''
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["pay","attention","practice","attend"]
        j = "at"
        o = 2
        self.assertEqual(s.prefixCount(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["leetcode","win","loops","success"]
        j = "code"
        o = 0
        self.assertEqual(s.prefixCount(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)