# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two integers dividend and divisor, divide two integers without
    using multiplication, division, and mod operator.

    The integer division should truncate toward zero, which means losing
    its fractional part.

    Return the quotient after dividing dividend by divisor.

    Note: assume the environment only stores 32-bit signed integers
    [-2^31, 2^31 - 1]. For this problem if the quotient is strictly
    greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is
    strictly less than -2^31, then return -2^31.
    '''
    # time limit exceeded (10/992 cases)
    def divide_timeout(self, dividend: int, divisor: int) -> int:
        st = dividend >= 0
        if not st:
            dividend = 0 - dividend 
        sb = divisor >= 0
        if not sb:
            divisor = 0 - divisor
        # how many times can divisor be subtracted from dividend
        # ie quotient
        q = 0
        while dividend >= divisor:
            dividend -= divisor
            q += 1
        # quotient is positive
        if st ^ sb:
            return 0 - q
        # quotient is negative
        else:
            return q

    def divide(self, dividend: int, divisor: int) -> int:
        # corner case where quotient could overflow boundaries
        if divisor == -1 and dividend == -2147483648:
            return 2147483647
        # determine if quotient should be positive
        positive = not (dividend >= 0) ^ (divisor >= 0)
        # force dividend and divisor to be positive
        # using abs function because it "could" be implemented without
        # multiplication operator
        dividend, divisor = abs(dividend), abs(divisor)
        # quotient to return
        q = 0
        # keep reducing dividend until it is less than divisor
        while dividend >= divisor:
            d, i = divisor, 1
            # find power 2 multiple of divisor less than dividend
            while dividend >= d:
                # use bit shift to multiply by two sneaky wise
                d <<= 1
                i <<= 1
            # decrement dividend
            dividend -= d >> 1
            q += i >> 1
        return q if positive else -q

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10
        j = 3
        o = 3
        self.assertEqual(s.divide(i, j), o)

    def test_two(self):
        s = Solution()
        i = 7
        j = -3
        o = -2
        self.assertEqual(s.divide(i, j), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = 1
        o = 1
        self.assertEqual(s.divide(i, j), o)

    def test_four(self):
        s = Solution()
        i = -2147483648
        j = -1
        o = 2147483647
        self.assertEqual(s.divide(i, j), o)

    def test_five(self):
        s = Solution()
        i = -2147483648
        j = 1
        o = -2147483648
        self.assertEqual(s.divide(i, j), o)

    def test_six(self):
        s = Solution()
        i = -1
        j = -1
        o = 1
        self.assertEqual(s.divide(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)