# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a date string in the form Day Month Year, where:
    * Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
    * Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
      "Aug", "Sep", "Oct", "Nov", "Dec"}.
    * Year is in the range [1900, 2100].

    Convert the date string to the format YYYY-MM-DD, where:
    * YYYY denotes the 4 digit year.
    * MM denotes the 2 digit month.
    * DD denotes the 2 digit day.
    '''
    month = {
        "Jan":"01",
        "Feb":"02",
        "Mar":"03",
        "Apr":"04",
        "May":"05",
        "Jun":"06",
        "Jul":"07",
        "Aug":"08",
        "Sep":"09",
        "Oct":"10",
        "Nov":"11",
        "Dec":"12"
        }
    def reformatDate(self, date: str) -> str:
        date = date.split()
        return f'{date[2]}-{self.month[date[1]]}-{"0" + date[0][0] if len(date[0]) == 3 else date[0][:2]}'

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "20th Oct 2052"
        o = "2052-10-20"
        self.assertEqual(s.reformatDate(i), o)

    def test_two(self):
        s = Solution()
        i = "6th Jun 1933"
        o = "1933-06-06"
        self.assertEqual(s.reformatDate(i), o)

    def test_three(self):
        s = Solution()
        i = "26th May 1960"
        o = "1960-05-26"
        self.assertEqual(s.reformatDate(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)