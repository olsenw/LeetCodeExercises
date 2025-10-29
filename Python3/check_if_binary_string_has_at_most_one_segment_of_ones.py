# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import re
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary string s without leading zeros, return true if s contains at
    most one contiguous segment of ones. Otherwise return false.
    '''
    def checkOnesSegment_regex(self, s: str) -> bool:
        return re.match("^0*1*0*$", s) is not None

    def checkOnesSegment_linear_scan(self, s: str) -> bool:
        ones = True
        i = 0
        while i < len(s):
            if ones and s[i] == '0':
                ones = False
            elif ones == False and s[i] == '1':
                return False
            i += 1
        return True

    def checkOnesSegment(self, s: str) -> bool:
        i = s.find('0')
        if i == -1:
            return True
        return s.find('1', i) == -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1001"
        o = False
        self.assertEqual(s.checkOnesSegment(i), o)

    def test_two(self):
        s = Solution()
        i = "110"
        o = True
        self.assertEqual(s.checkOnesSegment(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)