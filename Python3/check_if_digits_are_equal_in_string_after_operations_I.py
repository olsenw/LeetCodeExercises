# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of digits. Perform the following operation
    repeatedly until the string has exactly two digits:
    * For each pair of consecutive digits in s, starting from the first digit,
      calculate a new digit as the sum of the digits modulo 10.
    * Replace s with the sequence of newly calculated digits, maintaining the
      order which they are computed.

    Return true if the final two digits in s are the same; otherwise, return
    false.
    '''
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            a = ""
            for i in range(1, len(s)):
                a += str((int(s[i]) + int(s[i-1])) % 10)
            s = a
        return s[0] == s[1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "3902"
        o = True
        self.assertEqual(s.hasSameDigits(i), o)

    def test_two(self):
        s = Solution()
        i = "34789"
        o = False
        self.assertEqual(s.hasSameDigits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)