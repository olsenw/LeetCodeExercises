# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two arrays of strings that represent two inclusive events that
    happened on the same day, event1 and event2, where:
    * event1 = [startTime1, endTime1] and
    * event2 = [startTime2, endTime2].

    Event times are valid 24 hours format in the form of HH:MM.

    A conflict happens when two events have some non-empty intersection (ie,
    some moment is common to both events).

    Return true if there is a conflict between two events. Otherwise, return
    false.
    '''
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        s = lambda x: int(x[:2]) * 60 + int(x[3:])
        a,b = s(event1[0]), s(event1[1])
        c,d = s(event2[0]), s(event2[1])
        if a <= c:
            return c <= b
        return a <= d

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["01:15","02:00"], ["02:00","03:00"]
        o = True
        self.assertEqual(s.haveConflict(*i), o)

    def test_two(self):
        s = Solution()
        i = ["01:00","02:00"], ["01:20","03:00"]
        o = True
        self.assertEqual(s.haveConflict(*i), o)

    def test_three(self):
        s = Solution()
        i = ["10:00","11:00"], ["14:00","15:00"]
        o = False
        self.assertEqual(s.haveConflict(*i), o)

    def test_four(self):
        s = Solution()
        i = ["15:19","17:56"], ["14:11","20:02"]
        o = True
        self.assertEqual(s.haveConflict(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)