# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and a character letter, return the percentage of characters
    in s that equal letter rounded down to the nearest whole percent
    '''
    def percentageLetter(self, s: str, letter: str) -> int:
        return (s.count(letter) * 100) // len(s)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "foobar"
        j = "o"
        o = 33
        self.assertEqual(s.percentageLetter(i,j), o)

    def test_two(self):
        s = Solution()
        i = "jjjj"
        j = "k"
        o = 0
        self.assertEqual(s.percentageLetter(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)