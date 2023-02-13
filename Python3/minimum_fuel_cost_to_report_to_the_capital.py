# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set

class Solution:
    '''
    There is a tree (ie a connected, undirected graph with no cycles) structure
    country network consisting of n cities numbered from 0 to n - 1 and exactly
    n - 1 roads. The capital city is city 0. Given a 2D integer array roads
    where roads[i] = [ai, bi] denotes that there exists a bidirectional road 
    connecting cites ai and bi.

    There is a meeting for the representatives of each city. The meeting is in
    the capital city.

    There is a car in each city. Given an integer seats that indicates the
    number of seats in each car.

    A representative can use the car in their city to travel or change the car
    and ride with another representative. The cost of traveling between two
    cities is one liter of fuel.

    Return the minimum number of liters of fuel to reach the capital city.
    '''
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # amount of gas used
        answer = 0
        # graph in list form (know cities have numbers 0 to n-1)
        graph: List[List[int]] = [[] for _ in range(len(roads) + 1)]
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)
        # city currently in, previous city to prevent going backwards
        def dfs(city: int, last: int) -> int:
            nonlocal answer
            representatives = 1
            # how many representatives are in this city traveling to city 0
            for c in graph[city]:
                # don't backtrack
                if c == last:
                    continue
                representatives += dfs(c, city)
            # no travel gas needed if already in city 0
            if city > 0:
                # number of filled cars + unfilled cars
                answer += (representatives // seats) + (1 if representatives % seats else 0)
            return representatives
        dfs(0,-1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[0,2],[0,3]]
        j = 5
        o = 3
        self.assertEqual(s.minimumFuelCost(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
        j = 2
        o = 7
        self.assertEqual(s.minimumFuelCost(i,j), o)

    def test_three(self):
        s = Solution()
        i = []
        j = 1
        o = 0
        self.assertEqual(s.minimumFuelCost(i,j), o)

    def test_four(self):
        s = Solution()
        i = [[0,1],[0,2],[1,3],[1,4]]
        j = 5
        o = 4
        self.assertEqual(s.minimumFuelCost(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)