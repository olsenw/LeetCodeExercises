# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, return true if n has exactly three positive divisors.
    Otherwise, return false.

    An integer m is a divisor of n if there exists an integer k such that
    n = k * m.
    '''
    def isThree(self, n: int) -> bool:
        # l = list(n % i == 0 for i in range(1,n+1))
        # return sum(l) == 3
        return sum(n % i == 0 for i in range(1,n+1)) == 3

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        o = False
        self.assertEqual(s.isThree(i), o)

    def test_two(self):
        s = Solution()
        i = 4
        o = True
        self.assertEqual(s.isThree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)