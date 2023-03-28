# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a plan to travel by train made a year in advance. The days of the
    year on which travel will occur is given as an integer array days. Each day
    is an integer from 1 to 365.

    Train tickets are sold in three different ways:
    * a 1-day pass is sold for costs[0] dollars
    * a 7-day pass is sold for costs[1] dollars
    * a 30-day pass is sold for costs[2] dollars

    The passes allow that many days of consecutive travel.

    Return the minimum number of dollars that will need to be spent to travel
    every day in the given list of days.
    '''
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        @cache
        def cost(index: int) -> int:
            if index == n:
                return 0
            i = index + 1
            a = costs[0] + cost(i)
            while i < n and days[i] < days[index] + 7:
                i += 1
            b = costs[1] + cost(i)
            while i < n and days[i] < days[index] + 30:
                i += 1
            c = costs[2] + cost(i)
            return min(a,b,c)
        return cost(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4,6,7,8,20]
        j = [2,7,15]
        o = 11
        self.assertEqual(s.mincostTickets(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5,6,7,8,9,10,30,31]
        j = [2,7,15]
        o = 17
        self.assertEqual(s.mincostTickets(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)