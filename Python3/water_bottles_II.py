# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers numBottles and numExchange.

    numBottles represents the number of full water bottles that it is possible
    to start with. In one operation, one of the following actions can be taken:
    * Drink any number of full water bottles turning them into empty water
      bottles.
    * Exchange numExchange empty bottles with one full water bottle. Then
    increase numExchange by one.

    Note that it is not possible to exchange multiple batches of empty bottles
    for the same value of numExchange.

    Return the maximum number of water bottles that can be drank.
    '''
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        answer = numBottles
        while numBottles >= numExchange:
            numBottles = numBottles - numExchange + 1
            numExchange += 1
            answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 13
        j = 6
        o = 15
        self.assertEqual(s.maxBottlesDrunk(i,j), o)

    def test_two(self):
        s = Solution()
        i = 10
        j = 3
        o = 13
        self.assertEqual(s.maxBottlesDrunk(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)