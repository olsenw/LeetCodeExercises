# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an integer k.
    
    Reverse the first k characters of s and return the resulting string.
    '''
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcd"
        j = 2
        o = "bacd"
        self.assertEqual(s.reversePrefix(i,j), o)

    def test_two(self):
        s = Solution()
        i = "xyz"
        j = 3
        o = "zyx"
        self.assertEqual(s.reversePrefix(i,j), o)

    def test_three(self):
        s = Solution()
        i = "hey"
        j = 1
        o = "hey"
        self.assertEqual(s.reversePrefix(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)