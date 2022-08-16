# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    def __init__(self):
        self.h = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    def romanToInt(self, s: str) -> int:
        val = self.h[s[0]]
        last = val
        for v in s[1:]:
            c = self.h[v]
            if last < c:
                val -= 2 * last
            val += c
            last = c
        return val

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "III"
        o = 3
        self.assertEqual(s.romanToInt(i), o)

    def test_two(self):
        s = Solution()
        i = "LVIII"
        o = 58
        self.assertEqual(s.romanToInt(i), o)

    def test_three(self):
        s = Solution()
        i = "MCMXCIV"
        o = 1994
        self.assertEqual(s.romanToInt(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)