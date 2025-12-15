# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array prices representing the daily price history of a
    stock, where prices[i] is the stock price on the ith day.

    A smooth descent period of a stock consists of one or more contiguous days
    such that the price on each day is lower than the price on the preceding day
    by exactly 1. The first day of the period is exempted from this rule.

    Return the number of smooth descent periods.
    '''
    def getDescentPeriods(self, prices: List[int]) -> int:
        answer = 1
        running = 1
        for i in range(1, len(prices)):
            if prices[i] + 1 == prices[i-1]:
                running += 1
            else:
                running = 1
            answer += running
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,1,4]
        o = 7
        self.assertEqual(s.getDescentPeriods(i), o)

    def test_two(self):
        s = Solution()
        i = [8,6,7,7]
        o = 4
        self.assertEqual(s.getDescentPeriods(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = 1
        self.assertEqual(s.getDescentPeriods(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)