# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings order and s. All the characters are unique and were sorted
    in some custom order previously.

    Permute the characters of s so that they match the order that order was
    sorted. More specifically, if a character x occurs before a character y in
    order, then x should occur before y in the permuted string.

    Return any permutation of s that satisfies that property.
    '''
    def customSortString(self, order: str, s: str) -> str:
        key = {j:i for i,j in enumerate(order)}
        return "".join(sorted(s, key=lambda x: -1 if x not in key else key[x]))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "bcafg"
        j = "abcd"
        o = "bcad"
        self.assertEqual(s.customSortString(i,j), o)

    def test_two(self):
        s = Solution()
        i = "cba"
        j = "abcd"
        o = "cbad"
        self.assertEqual(s.customSortString(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)