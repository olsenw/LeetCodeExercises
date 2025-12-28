# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s representing a 12-hour format time where some of the digits
    (possibly none) are replaced with a "?".

    12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and
    MM is between 00 and 59. The earliest 12-hour time is 00:00, and the latest
    is 11:59.

    Replace all the "?" characters in s with digits such that the time obtained
    is a valid 12-hour formate time and is the latest possible.

    Return the resulting string.
    '''
    def findLatestTime(self, s: str) -> str:
        answer = ["?","?",":","?","?"]
        a,b,c,d = s[0],s[1],s[3],s[4]
        # hours
        if a == "?" and b == "?":
            answer[0] = "1"
            answer[1] = "1"
        elif a == "?":
            answer[1] = b
            if b > '1':
                answer[0] = "0"
            else:
                answer[0] = "1"
        elif b == "?":
            answer[0] = a
            if a == '0':
                answer[1] = "9"
            else:
                answer[1] = "1"
        else:
            answer[0] = a
            answer[1] = b
        # minutes
        if c == "?" and d == "?":
            answer[3] = "5"
            answer[4] = "9"
        elif c == "?":
            answer[3] = "5"
            answer[4] = d
        elif d == "?":
            answer[3] = c
            answer[4] = "9"
        else:
            answer[3] = c
            answer[4] = d
        return "".join(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1?:?4"
        o = "11:54"
        self.assertEqual(s.findLatestTime(i), o)

    def test_two(self):
        s = Solution()
        i = "0?:5?"
        o = "09:59"
        self.assertEqual(s.findLatestTime(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)