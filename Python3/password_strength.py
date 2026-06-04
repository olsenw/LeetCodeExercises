# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string password.

    The strength of the password is calculated based on the following rules:
    * 1 point for each distinct lowercase letter ('a' to 'z').
    * 2 points for each distinct uppercase letter ('A' to 'Z').
    * 3 points for each distinct digit ('0' to '9')
    * 5 points for each distinct special character from the set "!@#$".

    Each character contributes at most once, even if it appears multiple times.

    Return an integer denoting the strength of the password.
    '''
    def passwordStrength(self, password: str) -> int:
        values = dict()
        a = "abcdefghijklmnopqrstuvwxyz"
        for c in a:
            values[c] = 1
        for c in a.upper():
            values[c] = 2
        for c in "0123456789":
            values[c] = 3
        for c in "!@#$":
            values[c] = 5
        return sum(values[c] for c in set(password))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aA1!"
        o = 11
        self.assertEqual(s.passwordStrength(i), o)

    def test_two(self):
        s = Solution()
        i = "bbB11#"
        o = 11
        self.assertEqual(s.passwordStrength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)