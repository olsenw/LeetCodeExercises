# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string date representing a Gregorian calendar date formatted as
    YYYY-MM-DD, return the day number f the year
    '''
    def dayOfYear(self, date: str) -> int:
        calendar = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = date.split("-")
        year, month, day = int(year), int(month), int(day)
        if year > 1900 and year % 4 == 0:
            calendar[2] += 1
        return sum(calendar[i] for i in range(month)) + day

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "2019-01-09"
        o = 9
        self.assertEqual(s.dayOfYear(i), o)

    def test_two(self):
        s = Solution()
        i = "2019-02-10"
        o = 41
        self.assertEqual(s.dayOfYear(i), o)

    def test_three(self):
        s = Solution()
        # leap year
        i = "1904-12-31"
        o = 366
        self.assertEqual(s.dayOfYear(i), o)

    def test_four(self):
        s = Solution()
        i = "1905-12-31"
        o = 365
        self.assertEqual(s.dayOfYear(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)