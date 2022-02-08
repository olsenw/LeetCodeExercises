# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer num, repeatedly add all its digits until the result
    has only one digit, and return it.
    '''
    def addDigits_loop(self, num: int) -> int:
        while num > 9:
            n = 0
            while num > 9:
                n += num % 10
                num //= 10
            num = n + num
        return num

    # from leetcode solutions
    # https://leetcode.com/problems/add-digits/solution/
    # sneaky math trick...
    # https://en.wikipedia.org/wiki/Digital_root
    def addDigits_math(self, num: int) -> int:
        if num == 0: return 0
        if num % 9 == 0: return 9
        return num % 9
        # slightly slower
        # return 1 + (num - 1) % 9 if num else 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 38
        o = 2
        self.assertEqual(s.addDigits_loop(i), o)
        self.assertEqual(s.addDigits_math(i), o)

    def test_two(self):
        s = Solution()
        i = 0
        o = 0
        self.assertEqual(s.addDigits_loop(i), o)
        self.assertEqual(s.addDigits_math(i), o)

    def test_three(self):
        s = Solution()
        i = 4
        o = 4
        self.assertEqual(s.addDigits_loop(i), o)
        self.assertEqual(s.addDigits_math(i), o)

    def test_four(self):
        s = Solution()
        i = 1230
        o = 6
        self.assertEqual(s.addDigits_loop(i), o)
        self.assertEqual(s.addDigits_math(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)