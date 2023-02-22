# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A conveyor belt has packages that must be shipped from one port to another
    within days days.

    The ith package on the conveyor belt has a weight of weights[i]. Each day a
    ship is loaded via the the conveyor belt (in the order given by weights). It
    is not possible to load more weight than the maximum weight capacity of the
    ship.

    Return the least weight capacity of the ship that will result in all the
    packages on the conveyor belt being shipped within days days.
    '''
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # lower and upper bound on capacity of ship
        i,j = max(weights), sum(weights)
        # binary search all possible capacities
        while i < j:
            k = (j - i) // 2 + i
            c,d = 0,1
            for w in weights:
                if c + w > k:
                    d += 1
                    c = 0
                c += w
            if d > days:
                i = k + 1
            else:
                j = k
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5,6,7,8,9,10]
        j = 5
        o = 15
        self.assertEqual(s.shipWithinDays(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,2,2,4,1,4]
        j = 3
        o = 6
        self.assertEqual(s.shipWithinDays(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,1,1]
        j = 4
        o = 3
        self.assertEqual(s.shipWithinDays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)