# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given n coins, build a staircase using the coins. The staircase consists of
    k rows where the ith row has exactly i coins. The last row of the staircase
    may be incomplete.

    Given the integer n, return the number of complete rows of the constructed
    staircase.
    '''
    # lazy solution
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n >= i:
            n -= i
            i += 1
        return i - 1

    '''
    Can also do binary search to find the answer, number of coins used in a
    staircase can be determined by i * (i + 1) // 2
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        o = 2
        self.assertEqual(s.arrangeCoins(i), o)

    def test_two(self):
        s = Solution()
        i = 8
        o = 3
        self.assertEqual(s.arrangeCoins(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)