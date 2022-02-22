# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string columnTitle that represents the column titles as they
    appear in an Excel spread sheet, return its corresponding column
    number.
    '''
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        for c in columnTitle:
            number *= 26
            number += ord(c) - ord('A') + 1
        return number

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "A"
        o = 1
        self.assertEqual(s.titleToNumber(i), o)

    def test_two(self):
        s = Solution()
        i = "AB"
        o = 28
        self.assertEqual(s.titleToNumber(i), o)

    def test_three(self):
        s = Solution()
        i = "ZY"
        o = 701
        self.assertEqual(s.titleToNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)