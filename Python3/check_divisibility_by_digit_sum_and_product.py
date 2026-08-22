# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n. Determine whether n is divisible by the sum of
    the following two values:
    * The digit sum of n (the sum of its digits)
    * The digit product of n (the product of its digits)

    Return True if n is divisible by this sum; otherwise return false.
    '''
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        t = n
        while n:
            d,m = divmod(n, 10)
            n = d
            s += m
            p *= m
        return t % (s + p) == 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 99
        o = True
        self.assertEqual(s.checkDivisibility(i), o)

    def test_two(self):
        s = Solution()
        i = 23
        o = False
        self.assertEqual(s.checkDivisibility(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)