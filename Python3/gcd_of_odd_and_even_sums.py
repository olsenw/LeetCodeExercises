# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n. Compute the GCD (Greatest Common Divisor) of two values:
    * sumOdd: the sum of the smallest n positive odd numbers.
    * sumEven: the sum of the smallest n positive even numbers.

    Return the GCD of sumOdd and sumEven.
    '''
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        o = 4
        self.assertEqual(s.gcdOfOddEvenSums(i), o)

    def test_two(self):
        s = Solution()
        i = 5
        o = 5
        self.assertEqual(s.gcdOfOddEvenSums(i), o)

    def test_three(self):
        s = Solution()
        i = 800
        o = 800
        self.assertEqual(s.gcdOfOddEvenSums(i), o)

    def test_four(self):
        s = Solution()
        i = 1000
        o = 1000
        self.assertEqual(s.gcdOfOddEvenSums(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)