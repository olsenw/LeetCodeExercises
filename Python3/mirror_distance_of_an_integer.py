# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n.

    Define its mirror distance as: abs(n - reverse(n)) where reverse(n) is the
    integer formed by reversing the digits of n.

    Return an integer denoting the mirror distance of n.

    abs(x) denotes the absolute value of x.
    '''
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 25
        o = 27
        self.assertEqual(s.mirrorDistance(i), o)

    def test_two(self):
        s = Solution()
        i = 10
        o = 9
        self.assertEqual(s.mirrorDistance(i), o)

    def test_three(self):
        s = Solution()
        i = 7
        o = 0
        self.assertEqual(s.mirrorDistance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)