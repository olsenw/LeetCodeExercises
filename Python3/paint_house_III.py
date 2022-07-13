# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List
from functools import cache

class Solution:
    '''
    There is a row of m houses in a small city, each house must be
    painted with one of the n colors (labeled from 1 to n), some houses
    that have been painted last summer should not be painted again.

    A neighborhood is a maximal group of continuous houses that are
    painted with the same color.

    Given an array houses, an m x n matrix cost and an integer target
    where:
    * houses[i]: is the color of the house i, and 0 if the house is not
      painted yet.
    * cost[i][j]: is the cost of paint the house i with color j + 1.

    Return the minimum cost of painting all the remaining houses in such
    a way that there are exactly target neighborhoods. If it is not
    possible return -1.
    '''
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # Based on Top-down Leetcode solution
        # m possible houses, m possible neighborhoods, n possible colors
        @cache
        def dp(i, hoods, prev):
            # base case all houses checked
            if i == len(houses):
                return float('inf') if hoods != target else 0
            # base case too many neighborhoods
            if hoods > target:
                return float('inf')
            # recursion
            mcost = float('inf')
            # house is already painted
            if houses[i]:
                hood = hoods if prev == houses[i] else hoods + 1
                mcost = dp(i + 1, hood, houses[i])
            else:
                for color in range(1, n + 1):
                    hood = hoods if prev == color else hoods + 1
                    c = cost[i][color - 1] + dp(i+1,hood,color)
                    mcost = min(mcost, c)
            return mcost
        a = dp(0,0,0)
        return -1 if a == float('inf') else a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,0,0,0,0]
        j = [[1,10],[10,1],[10,1],[1,10],[5,1]]
        k = 5
        l = 2
        m = 3
        o = 9
        self.assertEqual(s.minCost(i,j,k,l,m), o)

    def test_two(self):
        s = Solution()
        i = [0,2,1,2,0]
        j = [[1,10],[10,1],[10,1],[1,10],[5,1]]
        k = 5
        l = 2
        m = 3
        o = 11
        self.assertEqual(s.minCost(i,j,k,l,m), o)

    def test_three(self):
        s = Solution()
        i = [3,1,2,3]
        j = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
        k = 4
        l = 3
        m = 3
        o = -1
        self.assertEqual(s.minCost(i,j,k,l,m), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)