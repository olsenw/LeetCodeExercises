# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are numBottles water bottles that are initially full of water. It is
    possible to exchange numExchange empty water bottles from the market with
    one full water bottle.

    The operation of drinking a full water bottle turns it into an empty bottle.

    Given the two integers numBottles and numExchange, return the maximum number
    of water bottles that can be drank.
    '''
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = numBottles
        while numBottles >= numExchange:
            d,r = divmod(numBottles, numExchange)
            answer += d
            numBottles = d + r
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 9
        j = 3
        o = 13
        self.assertEqual(s.numWaterBottles(i,j), o)

    def test_two(self):
        s = Solution()
        i = 15
        j = 4
        o = 19
        self.assertEqual(s.numWaterBottles(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)