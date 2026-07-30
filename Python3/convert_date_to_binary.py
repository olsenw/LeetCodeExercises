# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string date representing a Gregorian calendar date in the yyyy-mm-dd
    format.

    date can be written in its binary representation obtained by converting
    year, month, and day to their binary representations without any leading
    zeros and writing them down in year-month-day format.

    Return the binary representation of date.
    '''
    def convertDateToBinary(self, date: str) -> str:
        return f'{bin(int(date[:4]))[2:]}-{bin(int(date[5:7]))[2:]}-{bin(int(date[8:]))[2:]}'

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "2080-02-29"
        o = "100000100000-10-11101"
        self.assertEqual(s.convertDateToBinary(i), o)

    def test_two(self):
        s = Solution()
        i = "1900-01-01"
        o = "11101101100-1-1"
        self.assertEqual(s.convertDateToBinary(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)