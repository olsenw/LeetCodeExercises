# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array cost where cost[i] is the cost of ith step on
    a staircase. Once the cost is paid it is possible to climb one or
    two steps.

    It is possible to start from index 0 or from index 1.

    Return the minimum cost to reach the top of the floor.
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''Accepted'''
        for i in range(2,len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,15,20]
        o = 15
        self.assertEqual(s.minCostClimbingStairs(i), o)

    def test_two(self):
        s = Solution()
        i = [1,100,1,1,1,100,1,1,100,1]
        o = 6
        self.assertEqual(s.minCostClimbingStairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)