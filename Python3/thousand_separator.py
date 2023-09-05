# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, add a dot (".") as the thousands separator and return it
    in string format.
    '''
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        answer = s[-3:]
        s = s[:-3]
        while s:
            answer = s[-3:] + '.' + answer
            s = s[:-3]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 987
        o = "987"
        self.assertEqual(s.thousandSeparator(i), o)

    def test_two(self):
        s = Solution()
        i = 1234
        o = "1.234"
        self.assertEqual(s.thousandSeparator(i), o)

    def test_three(self):
        s = Solution()
        i = 123456789
        o = "123.456.789"
        self.assertEqual(s.thousandSeparator(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)