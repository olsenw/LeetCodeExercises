# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed string s that has lowercase English letters in its even
    indices and digits in its odd indices.

    There is a function shift(c,x), where c is a character and x is a digit,
    that returns the xth character after c.

    For every odd index i, replace the digit s[i] with shift(s[i-1], s[i]).

    Return s after replacing all digits. It is guaranteed that
    shifts(s[i-1], s[i]) will never exceed 'z'
    '''
    def replaceDigits(self, s: str) -> str:
        def shift(c, x):
            # c = ord(c) - ord('a')
            # x = ord(x) - ord('0')
            # return chr(c + x + ord('a'))
            return chr(ord(c) + ord(x) - ord('0'))
        return ''.join(shift(s[i-1], s[i]) if i % 2 else s[i] for i in range(len(s)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "a1c1e1"
        o = "abcdef"
        self.assertEqual(s.replaceDigits(i), o)

    def test_two(self):
        s = Solution()
        i = "a1b2c3d4e"
        o = "abbdcfdhe"
        self.assertEqual(s.replaceDigits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)