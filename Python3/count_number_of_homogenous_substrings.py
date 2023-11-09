# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, return the number of homogenous substrings of s. Since the
    answer may be too large, return it modulo 10^9 + 7.

    A string is homogenous if all the characters of the string are the same.

    A substring is a contiguous sequence of characters within a string.
    '''
    def countHomogenous(self, s: str) -> int:
        m = 10**9 + 7
        n = len(s)
        a = [1] * n
        for i in range(1, n):
            if s[i] == s[i-1]:
                a[i] += a[i-1]
        return sum(a) % m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abbcccaa"
        o = 13
        self.assertEqual(s.countHomogenous(i), o)

    def test_two(self):
        s = Solution()
        i = "xy"
        o = 2
        self.assertEqual(s.countHomogenous(i), o)

    def test_three(self):
        s = Solution()
        i = "zzzzz"
        o = 15
        self.assertEqual(s.countHomogenous(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)