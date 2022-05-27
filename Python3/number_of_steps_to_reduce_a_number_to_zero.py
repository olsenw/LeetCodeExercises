# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    def numberOfSteps_simulation(self, num: int) -> int:
        s = 0
        while num:
            s += 1
            if num & 1:
                num -= 1
            else:
                num //= 2
        return s

    def numberOfSteps_bitshift(self, num: int) -> int:
        if num < 2:
            return num
        s = 1
        while num > 1:
            s += 2 if num & 1 else 1
            num >>= 1
        return s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 14
        o = 6
        self.assertEqual(s.numberOfSteps(i), o)

    def test_two(self):
        s = Solution()
        i = 8
        o = 4
        self.assertEqual(s.numberOfSteps(i), o)

    def test_three(self):
        s = Solution()
        i = 123
        o = 12
        self.assertEqual(s.numberOfSteps(i), o)

    def test_four(self):
        s = Solution()
        i = 0
        o = 0
        self.assertEqual(s.numberOfSteps(i), o)

    def test_five(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.numberOfSteps(i), o)

    def test_six(self):
        s = Solution()
        i = 2
        o = 2
        self.assertEqual(s.numberOfSteps(i), o)

    def test_seven(self):
        s = Solution()
        i = 3
        o = 3
        self.assertEqual(s.numberOfSteps(i), o)

    def test_eight(self):
        s = Solution()
        i = 4
        o = 3
        self.assertEqual(s.numberOfSteps(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)