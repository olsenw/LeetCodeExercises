# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array prices representing the prices of various chocolates
    in a store. Also given is a single integer money, which represents an
    initial amount of money.

    Buy exactly two chocolates in such a way that there is some non-negative
    leftover money. Minimize the sum of prices of the purchased chocolates.

    Return the amount of money leftover after buying two chocolates. If there is
    no way to buy two chocolates without ending up in debt, return money. Note
    that the leftover must be non-negative.
    '''
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        chocolates = money - prices[0] - prices[1]
        return chocolates if chocolates >= 0 else money

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)