# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers n and t. Return the smallest number greater than or equal
    to n such that the product of its digits is divisible by t.
    '''
    def smallestNumber_brute(self, n: int, t: int) -> int:
        def f(x):
            p = 1
            while x > 0:
                p *= x % 10
                x //= 10
            return p
        while f(n) % t != 0:
            n += 1
        return n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10, 2
        o = 10
        self.assertEqual(s.smallestNumber(*i), o)

    def test_two(self):
        s = Solution()
        i = 15, 3
        o = 16
        self.assertEqual(s.smallestNumber(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)