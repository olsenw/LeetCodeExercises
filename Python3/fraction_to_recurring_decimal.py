# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers representing the numerator and denominator of a fraction,
    return the fraction in string format.

    If the fractional part is repeating, enclose the repeating part in
    parentheses.

    If multiple answers are possible, return any of them.

    It is guaranteed that the length of the answer string is less than 10^4 for
    all the given inputs.
    '''
    # based on solution by Marlen09
    # https://leetcode.com/problems/fraction-to-recurring-decimal/solutions/3208837/166-solution-with-step-by-step-explanation/
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # edge case 0 divide by anything is 0
        if numerator == 0:
            return '0'
        # build answer
        answer = ""
        # answer will be negative
        if (numerator < 0) ^ (denominator < 0):
            answer += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        # result and remainder (ie integer part and decimal part)
        a,b = divmod(numerator, denominator)
        answer += str(a)
        # no more decimal, return early
        if b == 0:
            return answer
        answer += "."
        # check if pattern repeats
        repeat = {}
        # go until no more decimal or repeating pattern
        while b != 0 and b not in repeat:
            repeat[b] = len(answer)
            a,b = divmod(b * 10, denominator)
            answer += str(a)
        # repeating pattern
        if b in repeat:
            # non repeating section and the repeating section
            answer = f'{answer[:repeat[b]]}({answer[repeat[b]:]})'
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        j = 2
        o = "0.5"
        self.assertEqual(s.fractionToDecimal(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = 1
        o = "2"
        self.assertEqual(s.fractionToDecimal(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = 333
        o = "0.(012)"
        self.assertEqual(s.fractionToDecimal(i,j), o)

    def test_four(self):
        s = Solution()
        i = 4
        j = 9
        o = "0.(4)"
        self.assertEqual(s.fractionToDecimal(i,j), o)

    def test_five(self):
        s = Solution()
        i = -50
        j = 8
        o = "-6.25"
        self.assertEqual(s.fractionToDecimal(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)