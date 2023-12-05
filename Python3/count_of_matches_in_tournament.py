# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, representing the number of teams in a tournament that
    has strange rules:
    * If the current number of teams is even, each team gets paired with another
      team. A total of n / 2 matches are played, and n / 2 teams advance to the
      next round.
    * If the current number of teams is odd, one team randomly advances in the
      tournament, and the rest get paired. A total of (n-1) / 2 matches are
      played, and (n - 1) / 2 + 1 teams advance to the next round.

    Return the number of matches played in the tournament until a winner is
    decided.
    '''
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        # if n % 2:
        #     return n // 2 + self.numberOfMatches(n // 2 + 1)
        # else:
        #     return n // 2 + self.numberOfMatches(n // 2)
        return n // 2 + self.numberOfMatches(n // 2 + n % 2)

    # math
    def numberOfMatches_maths(self, n: int) -> int:
        return n - 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 7
        o = 6
        self.assertEqual(s.numberOfMatches(i), o)

    def test_two(self):
        s = Solution()
        i = 14
        o = 13
        self.assertEqual(s.numberOfMatches(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)