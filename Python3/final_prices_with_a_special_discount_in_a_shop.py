# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array prices where prices[i] is the price of the ith item
    in a shop.

    There is a special discount for items in the shop. If the ith item is
    bought, the a discount equivalent to prices[j] is applied where j is the
    minimum index such that j > i and prices[j] <= prices[i]. Otherwise there is
    no discount at.

    Return an integer array answer where answer[i] is the final price paid for
    the ith item of the shop, considering the special discount.
    '''
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            answer.append(prices[i] - discount)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [8,4,6,2,3]
        o = [4,2,4,2,3]
        self.assertEqual(s.finalPrices(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = [1,2,3,4,5]
        self.assertEqual(s.finalPrices(i), o)

    def test_three(self):
        s = Solution()
        i = [10,1,1,6]
        o = [9,0,1,6]
        self.assertEqual(s.finalPrices(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)