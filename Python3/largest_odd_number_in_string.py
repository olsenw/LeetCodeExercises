# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string num, representing a large integer. Return the largest-valued
    odd integer (as a string) that is a non-empty substring of num, or an empty
    string if no odd integer exists.
    '''
    def largestOddNumber_passes(self, num: str) -> str:
        n = len(num)
        for i in range(n - 1, -1, -1):
            if num[i] in "13579":
                return num[:i+1]
        return ""

    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if ord(num[i]) % 2:
                return num[:i+1]
        return ""

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "52"
        o = "5"
        self.assertEqual(s.largestOddNumber(i), o)

    def test_two(self):
        s = Solution()
        i = "4206"
        o = ""
        self.assertEqual(s.largestOddNumber(i), o)

    def test_three(self):
        s = Solution()
        i = "35427"
        o = "35427"
        self.assertEqual(s.largestOddNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)