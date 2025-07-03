# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s representing an attendance record for a student where each
    character signifies whether the student was absent, late, or present on that
    day. The record only contains the following three characters:
    * 'A': Absent
    * 'L': Late
    * 'P': Present

    The student is eligible for an attendance award if they meet both of the
    following criteria:
    * The student was absent ('A') for strictly fewer than 2 days total.
    * The student was never ('L') for 3 or more consecutive days.

    Return true if the student is eligible for an attendance award or false
    otherwise.
    '''
    def checkRecord(self, s: str) -> bool:
        a = False
        l = 0
        for c in s:
            if c == 'A':
                if a:
                    return False
                a = True
            if c == 'L':
                l += 1
                if l == 3:
                    return False
            else:
                l = 0
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "PPALLP"
        o = True
        self.assertEqual(s.checkRecord(i), o)

    def test_two(self):
        s = Solution()
        i = "PPALLL"
        o = False
        self.assertEqual(s.checkRecord(i), o)

    def test_three(self):
        s = Solution()
        i = "LALL"
        o = True
        self.assertEqual(s.checkRecord(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)