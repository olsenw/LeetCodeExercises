# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an alphanumeric string s, return the second largest numerical digit
    that appears in s, or -1 if it does not exist.

    An alphanumeric string is a string consisting of lowercase English letters
    and digits.
    '''
    def secondHighest(self, s: str) -> int:
        a,b = '/', '/'
        for c in s:
            if c.isnumeric():
                if c > a:
                    b,a = a,c
                elif c < a and c > b:
                    b = c

        if b == '/':
            return -1
        return int(b)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "dfa12321afd"
        o = 2
        self.assertEqual(s.secondHighest(i), o)

    def test_two(self):
        s = Solution()
        i = "abc1111"
        o = -1
        self.assertEqual(s.secondHighest(i), o)

    def test_three(self):
        s = Solution()
        i = "sjhtz8344"
        o = 4
        self.assertEqual(s.secondHighest(i), o)


if __name__ == '__main__':
    unittest.main(verbosity=2)