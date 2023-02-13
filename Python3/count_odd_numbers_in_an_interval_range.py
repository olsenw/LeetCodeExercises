# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two non-negative integers low and high. Return the count of odd
    numbers between low and high (inclusive).

    0 <= low <= high <= 10^9
    '''
    def countOdds(self, low: int, high: int) -> int:
        return (high // 2) - (low // 2) + (high % 2)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = 7
        o = 3
        self.assertEqual(s.countOdds(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 7
        o = 3
        self.assertEqual(s.countOdds(i,j), o)

    def test_three(self):
        s = Solution()
        i = 0
        j = 0
        o = 0
        self.assertEqual(s.countOdds(i,j), o)

    def test_four(self):
        s = Solution()
        i = 0
        j = 7
        o = 4
        self.assertEqual(s.countOdds(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)