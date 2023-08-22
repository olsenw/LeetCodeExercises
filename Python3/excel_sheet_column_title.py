# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer columnNumber, return its corresponding column title as it
    appears in an Excel sheet.
    '''
    # needed help on how to take a base 26 (starts at 0) move it starting at one
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""
        while columnNumber:
            columnNumber -= 1
            answer += chr(columnNumber % 26 + 65)
            columnNumber //= 26
        return answer[::-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = "A"
        self.assertEqual(s.convertToTitle(i), o)

    def test_two(self):
        s = Solution()
        i = 28
        o = "AB"
        self.assertEqual(s.convertToTitle(i), o)

    def test_three(self):
        s = Solution()
        i = 701
        o = "ZY"
        self.assertEqual(s.convertToTitle(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)