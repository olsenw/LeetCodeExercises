# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Implement pow(x,n) which calculates x raised to the power n (ie x^n).
    '''
    def myPow_trivial(self, x: float, n: int) -> float:
        #return math.pow(x, n)
        return x ** n

    def myPow_brute(self, x: float, n: int) -> float:
        answer = 1.0
        if n < 0:
            x = 1 / x
            n *= -1
        for _ in range(1, n + 1):
            answer *= x
        return answer

    # O(log(n))
    # based off of solution by 3anmoi3
    # https://leetcode.com/problems/powx-n/solutions/2951059/concise-simple-iterative-c-without-binary-shift/
    # had basic idea was unsure how to deal with excess case
    def myPow(self, x: float, n: int) -> float:
        # trivial cases
        if n == 0 or x == 1.0:
            return 1.0
        if x == 0.0:
            return 0.0
        # iterative log n solve
        answer = 1.0
        i = abs(n)
        while i:
            if i % 2 != 0:
                answer *= x
            x *= x
            i //= 2
        return 1.0 / answer if n < 0 else answer

    '''
    could probably improve the speed using bit shifting...
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2.0
        j = 10
        o = 1024.0
        self.assertEqual(round(s.myPow(i, j), 5), o)

    def test_two(self):
        s = Solution()
        i = 2.1
        j = 3
        o = 9.261
        self.assertEqual(round(s.myPow(i, j), 5), o)

    def test_three(self):
        s = Solution()
        i = 2.0
        j = -2
        o = 0.25
        self.assertEqual(round(s.myPow(i, j), 5), o)

    def test_four(self):
        s = Solution()
        i = 2.0
        j = 0
        o = 1.0
        self.assertEqual(round(s.myPow(i, j), 5), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)