# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given n x m grid and an integer k.

    A sensor placed on cell (r,c) covers all cells whose Chebyshev distance from
    (r,c) is at most k.

    The Chebyshev distance between two cells (r1,c1) and (r2,c2) is
    max(|r1-r2|,|c1-c2|).

    Return the minimum number of sensors required to cover eery cell of the
    grid.
    '''
    # based on hints
    def minSensors(self, n: int, m: int, k: int) -> int:
        s = 2 * k + 1
        return math.ceil(n / s) * math.ceil(m / s)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5,5,1
        o = 4
        self.assertEqual(s.minSensors(*i), o)

    def test_two(self):
        s = Solution()
        i = 2,2,2
        o = 1
        self.assertEqual(s.minSensors(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)