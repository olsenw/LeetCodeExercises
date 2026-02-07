# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting only of the characters '1' and '2'.

    It is possible to delete any number of characters from s without changing
    the order of the remaining character.

    Return the largest possible resultant string that represents an even
    integer. If there is no such string, return the empty string "".
    '''
    def largestEven(self, s: str) -> str:
        s = list(s)
        while s and s[-1] == '1':
            s.pop()
        return "".join(s)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1112"
        o = "1112"
        self.assertEqual(s.largestEven(i), o)

    def test_two(self):
        s = Solution()
        i = "221"
        o = "22"
        self.assertEqual(s.largestEven(i), o)

    def test_three(self):
        s = Solution()
        i = "1"
        o = ""
        self.assertEqual(s.largestEven(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)