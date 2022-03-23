# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a broken calculator that has the integer startValue on its
    display initially. In one operation it can:
    * multiply the number on display by 2
    * subtract 1 from the number on display

    Given two integers startValue and target, return the minimum number
    of operations needed to display target on the calculator.
    '''
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0
        # faster than startValue < target:
        while target > startValue:
            if target % 2:
                target += 1
            else:
                target //= 2
            ops += 1
        return ops + startValue - target

    def brokenCalc_timeout(self, startValue: int, target: int) -> int:
        ops = 0
        while startValue != target:
            if startValue > target or target % 2:
                target += 1
            else:
                target //= 2
            ops += 1
        return ops

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = 3
        o = 2
        self.assertEqual(s.brokenCalc(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = 8
        o = 2
        self.assertEqual(s.brokenCalc(i,j), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = 10
        o = 3
        self.assertEqual(s.brokenCalc(i,j), o)

    def test_four(self):
        s = Solution()
        i = 10
        j = 10
        o = 0
        self.assertEqual(s.brokenCalc(i,j), o)

    def test_five(self):
        s = Solution()
        i = 5
        j = 11
        o = 5
        self.assertEqual(s.brokenCalc(i,j), o)

    def test_six(self):
        s = Solution()
        i = 1000000000
        j = 1
        o = 999999999
        self.assertEqual(s.brokenCalc(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)