# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are two types of soup: type A and type B. Initially, there are n ml of
    each type of soup. There are four kinds of operations.
    1. Serve 100 ml of soup A and  0 ml of soup B,
    2. Serve  75 ml of soup A and 25 ml of soup B,
    3. Serve  50 ml of soup A and 50 ml of soup B,
    4. Serve  25 ml of soup A and 75 ml of soup B.

    When soup is served, it is gone. Each turn, an operation is chosen randomly
    from the four choices. If the remaining volume of soup is not enough to
    complete the operation, serve as much as possible. Stop when one of the
    volumes of soup becomes zero.

    Note that there is not an operation where 100ml of soup B is used first.

    Return the probability that soup A will be empty first, plus half the
    probability that A and B become empty at the same time. Answers within 10^-5
    of the actual answer will be accepted.
    '''
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0
        @cache
        def dp(a,b):
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1.0
            elif b <= 0:
                return 0.0
            else:
                return 0.25 * (dp(a-100,b) + dp(a-75,b-25) + dp(a-50,b-50) + dp(a-25,b-75))
        return dp(n,n)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 50
        o = 0.62500
        self.assertEqual(s.soupServings(i), o)

    def test_two(self):
        s = Solution()
        i = 100
        o = 0.71875
        self.assertEqual(s.soupServings(i), o)

    def test_three(self):
        s = Solution()
        i = 5000
        o = 1.0
        self.assertAlmostEqual(s.soupServings(i), o, 5)

    def test_four(self):
        s = Solution()
        i = 10000
        o = 1.0
        self.assertAlmostEqual(s.soupServings(i), o, 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)