# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a positive integer num consisting only of digits 6 and 9.

    Return the maximum number that can be obtained by changing at most one digit
    (6 becomes 9, and 9 becomes 6).
    '''
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        for i in range(len(s)):
            if s[i] == '6':
                return int(s[:i] + '9' + s[i+1:])
        return num

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 9669
        o = 9969
        self.assertEqual(s.maximum69Number(i), o)

    def test_two(self):
        s = Solution()
        i = 9996
        o = 9999
        self.assertEqual(s.maximum69Number(i), o)

    def test_three(self):
        s = Solution()
        i = 9999
        o = 9999
        self.assertEqual(s.maximum69Number(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)