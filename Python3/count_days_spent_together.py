# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob are traveling to Rome for separate business meetings.

    Given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will
    be in the city from the dates arriveAlice to leaveAlice (inclusive), while
    Bob will be in the city from the dates arriveBob to leaveBob (inclusive).
    Each will be a 5-character string in the format "MM-DD", corresponding to
    the month and day of the date.

    Return the total number of days that Alice and Bob are in Rome together.

    Assume that all dates occur in the same calendar year, which is not a leap
    year. Note that the number of days per month can be represented as: [31, 28,
    31, 30, 31, 30, 31, 31, 30, 31, 30, 31].
    '''
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        d = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        a = d[int(arriveAlice[:2])] + int(arriveAlice[3:]), d[int(leaveAlice[:2])] + int(leaveAlice[3:])
        b = d[int(arriveBob[:2])] + int(arriveBob[3:]), d[int(leaveBob[:2])] + int(leaveBob[3:])
        if a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]:
            return min(a[1], b[1]) - max(a[0],b[0]) + 1
        return 0
 
class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "08-15", "08-18", "08-16", "08-19"
        o = 3
        self.assertEqual(s.countDaysTogether(*i), o)

    def test_two(self):
        s = Solution()
        i = "10-01", "10-31", "11-01", "12-31"
        o = 0
        self.assertEqual(s.countDaysTogether(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)