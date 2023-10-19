# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A perfect number is a positive integer that is equal to the sum of it
    positive divisors, excluding the number itself. A divisor of an integer x is
    an integer that can divide x evenly.

    Given an integer n, return true if n is a perfect number, otherwise return
    false.
    '''
    # O(n) which is way too slow
    def checkPerfectNumber_too_slow(self, num: int) -> bool:
        decrement = num
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                decrement -= i
        return decrement == 0

    # O(sqrt(n))
    def checkPerfectNumber(self, num: int) -> bool:
        s = 0
        i = 1
        while i * i <= num:
            if num % i == 0:
                s += i
                if i * i != num:
                    s += num / i
            i += 1
        return s - num == num

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 28
        o = True
        self.assertEqual(s.checkPerfectNumber(i), o)

    def test_two(self):
        s = Solution()
        i = 7
        o = False
        self.assertEqual(s.checkPerfectNumber(i), o)

    def test_three(self):
        s = Solution()
        i = 99999995
        o = False
        self.assertEqual(s.checkPerfectNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)