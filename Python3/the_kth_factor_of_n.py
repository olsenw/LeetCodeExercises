# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two possible integers na dn k. A factor of an integer n is defined as
    an integer i where n % i = 0.

    Consider a list of all factors of n sorted in ascending order, return the
    kth factor in this list or return -1 if n has less than k factors.
    '''
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n+1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 12
        j = 3
        o = 3
        self.assertEqual(s.kthFactor(i,j), o)

    def test_two(self):
        s = Solution()
        i = 7
        j = 2
        o = 7
        self.assertEqual(s.kthFactor(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = 4
        o = -1
        self.assertEqual(s.kthFactor(i,j), o)

    def test_four(self):
        s = Solution()
        i = 4
        j = 1
        o = 1
        self.assertEqual(s.kthFactor(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = 1
        o = 1
        self.assertEqual(s.kthFactor(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)