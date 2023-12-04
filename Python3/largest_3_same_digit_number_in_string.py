# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string num representing a large integer. An integer is good if it
    meets the following conditions:
    * It is a substring of num with length 3.
    * It consists of only one unique digit.

    Return the maximum good integer as a string or an empty string "" if no such
    integer exists.

    Note:
    * A substring is a contiguous sequence of characters within a string.
    * There may be leading zeros in num or a good integer.
    '''
    def largestGoodInteger(self, num: str) -> str:
        answer = '/'
        running = 1
        current = num[0]
        for n in num[1:]:
            if n == current:
                running += 1
            else:
                current = n
                running = 1
            if running >= 3:
                answer = max(answer, current)
        return '' if answer == '/' else answer * 3

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "6777133339"
        o = "777"
        self.assertEqual(s.largestGoodInteger(i), o)

    def test_two(self):
        s = Solution()
        i = "2300019"
        o = "000"
        self.assertEqual(s.largestGoodInteger(i), o)

    def test_three(self):
        s = Solution()
        i = "42352338"
        o = ""
        self.assertEqual(s.largestGoodInteger(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)