# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer number n, return the difference between the product of its
    digits and the sum of its digits.
    '''
    def subtractProductAndSum(self, n: int) -> int:
        m = 1
        s = 0
        while n:
            d = n % 10
            n //= 10
            s += d
            m *= d
        return m - s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 234
        o = 15
        self.assertEqual(s.subtractProductAndSum(i), o)

    def test_two(self):
        s = Solution()
        i = 4421
        o = 21
        self.assertEqual(s.subtractProductAndSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)