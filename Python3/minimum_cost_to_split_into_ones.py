# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n.

    In one operation, it is possible to split an integer x into two positive
    integers a and b such that a + b = x.

    The cost of this operation is a * b.

    Return an integer denoting the minimum total cost required to split the
    integer n into n ones.
    '''
    # very slow
    @cache
    def minCost_dp(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        answer = float('inf')
        for i in range(1, n-1):
            answer = min(answer, (i * (n-i)) + self.minCost(i) + self.minCost(n - i))
        return answer

    # based on hint for math
    def minCost(self, n: int) -> int:
        return sum(i for i in range(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        o = 3
        self.assertEqual(s.minCost(i), o)

    def test_two(self):
        s = Solution()
        i = 4
        o = 6
        self.assertEqual(s.minCost(i), o)

    def test_three(self):
        s = Solution()
        i = 500
        o = 124750
        self.assertEqual(s.minCost(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)