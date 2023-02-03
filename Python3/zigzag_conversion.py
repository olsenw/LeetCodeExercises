# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import itertools
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
    of rows like this:

    P   A   H   N
    A P L S I I G
    Y   I   R

    And then read line by line "PAHNAPLSIIGYIR".

    Write the code that will take a string and this conversion given a number of
    rows.
    '''
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows
        i = itertools.cycle(list(range(numRows)) + list(range(numRows-2,0,-1)))
        for c in s:
            rows[next(i)] += c
        return "".join(rows)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "PAYPALISHIRING"
        j = 3
        o = "PAHNAPLSIIGYIR"
        self.assertEqual(s.convert(i,j), o)

    def test_two(self):
        s = Solution()
        i = "PAYPALISHIRING"
        j = 4
        o = "PINALSIGYAHRPI"
        self.assertEqual(s.convert(i,j), o)

    def test_three(self):
        s = Solution()
        i = "A"
        j = 1
        o = "A"
        self.assertEqual(s.convert(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)