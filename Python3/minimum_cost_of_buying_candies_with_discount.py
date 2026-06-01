# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A shop is selling candies at a discount. For every two candies sold, the
    shop gives a third candy for free.

    The customer can choose any candy to take away for free as long as the cost
    of the chosen candy is less than or equal to the minimum cost of the two 
    candies bought.

    Given a 0-indexed integer array cost, where cost[i] denotes the cost of the
    ith candy, return the minimum cost of buying all the candies.
    '''
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        answer = 0
        for i in range(len(cost)):
            if i % 3 < 2:
                answer += cost[i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = 5
        self.assertEqual(s.minimumCost(i), o)

    def test_two(self):
        s = Solution()
        i = [6,5,7,9,2,2]
        o = 23
        self.assertEqual(s.minimumCost(i), o)

    def test_three(self):
        s = Solution()
        i = [5,5]
        o = 10
        self.assertEqual(s.minimumCost(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)