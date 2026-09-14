# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters.

    The score of a string is the sum of the positions of its characters in the
    alphabet, where 'a'=1, 'b'=2, ..., 'z'=26.
    
    Determine whether there exists an index i such that the string can be split
    into two non-empty substrings s[0..i] and s[(i+1)..(n-1)] that have equal
    scores.

    Return True if such a split exists, otherwise return False.
    '''
    def scoreBalance(self, s: str) -> bool:
        total = sum(ord(c) - 96 for c in s)
        score = 0
        for c in s:
            score += ord(c) - 96
            total -= ord(c) - 96
            if score == total:
                return True
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "adcb"
        o = True
        self.assertEqual(s.scoreBalance(i), o)

    def test_two(self):
        s = Solution()
        i = "bace"
        o = False
        self.assertEqual(s.scoreBalance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)