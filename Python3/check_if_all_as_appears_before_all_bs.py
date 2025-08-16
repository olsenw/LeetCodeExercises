# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of only the characters 'a' and 'b;, return true
    if every 'a' appears before every 'b' in the string. Otherwise, return
    false.
    '''
    def checkString(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i] == 'a' and s[i-1] == 'b':
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aaabbb"
        o = True
        self.assertEqual(s.checkString(i), o)

    def test_two(self):
        s = Solution()
        i = "abab"
        o = False
        self.assertEqual(s.checkString(i), o)

    def test_three(self):
        s = Solution()
        i = "bbb"
        o = True
        self.assertEqual(s.checkString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)