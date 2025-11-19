# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string number representing a positive integer and a character digit.

    Return the resulting string after removing exactly one occurrence of digit
    from number such that the value of the resulting string in decimal form is
    maximized. The test cases are generated such that digit occurs at least once
    in number.
    '''
    def removeDigit(self, number: str, digit: str) -> str:
        answer = 0
        for i in range(len(number)):
            if number[i] == digit:
                answer = max(answer, int(number[:i] + number[i+1:]))
        return str(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "123"
        j = "3"
        o = "12"
        self.assertEqual(s.removeDigit(i,j), o)

    def test_two(self):
        s = Solution()
        i = "1231"
        j = "1"
        o = "231"
        self.assertEqual(s.removeDigit(i,j), o)

    def test_three(self):
        s = Solution()
        i = "551"
        j = "5"
        o = "51"
        self.assertEqual(s.removeDigit(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)