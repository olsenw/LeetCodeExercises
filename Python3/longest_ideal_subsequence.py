# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase letters and an integer k. A string
    t is ideal if the following conditions are satisfied:
    * t is a subsequence of the string s.
    * The absolute difference in the alphabet order of every two adjacent
      letters in t is less than or equal to k.
    
    Return the length of the longest ideal string.

    A subsequence is a string that can be derived from another string by
    deleting some or no characters without changing the order of the remaining
    characters.

    Note that the alphabet order is not cyclic. For example the absolute
    difference in the alphabet order of 'a' and 'z' is 25, not 1.
    '''
    def longestIdealString(self, s: str, k: int) -> int:
        h = {i:0 for i in "abcdefghijklmnopqrstuvwxyz"}
        for i,j in enumerate(s):
            n = ord(j) - 97
            pass
            # for x in range(min(0, n - k), max(n + k + 1,25)):
                # y = chr(x + 97)
            h[j] = max(h[j], 1 + max((h[chr(x + 97)] for x in range(max(0, n - k), min(n + k,25) + 1)),default=0))
        return max(h.values())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "acfgbd"
        j = 2
        o = 4
        self.assertEqual(s.longestIdealString(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abcd"
        j = 3
        o = 4
        self.assertEqual(s.longestIdealString(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)