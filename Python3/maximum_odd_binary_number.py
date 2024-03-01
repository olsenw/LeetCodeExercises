# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary string s that contains at least one '1'.

    Rearrange the bits in such a way that the resulting binary number is the
    maximum odd binary number that can be created from this combination.

    Return a string representing the maximum odd binary number that can be
    created from the given combination.

    Note that the resulting string can have leading zeros.
    '''
    def maximumOddBinaryNumber(self, s: str) -> str:
        a = s.count('1')
        return "1" * (a - 1) + "0" * (len(s) - a) + "1"

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "010"
        o = "001"
        self.assertEqual(s.maximumOddBinaryNumber(i), o)

    def test_two(self):
        s = Solution()
        i = "0101"
        o = "1001"
        self.assertEqual(s.maximumOddBinaryNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)