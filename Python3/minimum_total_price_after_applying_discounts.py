# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays prices and discounts.

    The value of prices[i] represents the price of the ith item, and
    discounts[j] represents the discount percentage.

    It is possible to apply discounts subject to the following rules:
    * Each discount can be applied to at most one item.
    * Each item can receive at most one discount.
    * An item may also receive no discount.

    If a discount of d percent is applied to an item with price p, its final
    price becomes (p * (100 - d)) / 100. The final price is not rounded.

    Return the minimum possible sum of final prices after assigning discounts
    optimally. Answers withing 1p^-5 of the actual answer will be accepted.
    '''
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        discounts.extend([0] * (len(prices) - len(discounts)))
        def price(p:int, d:int) -> float:
            return (p * (100 - d)) / 100
        return sum(price(p,d) for p,d in zip(prices, discounts))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,30,21]
        j = [50,60]
        o = 32.50000
        self.assertEqual(s.minPrice(i,j), o)

    def test_two(self):
        s = Solution()
        i = [100,70]
        j = [10,40,50]
        o = 92.0
        self.assertEqual(s.minPrice(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)