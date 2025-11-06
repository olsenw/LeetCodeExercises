# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedSet

class Solution:
    '''
    Given an integer c representing c power stations, each with a unique
    identifier id from 1 to c (1-based indexing).

    These stations are interconnected via n, bidirectional cables, represented
    by a 2D array connections, where each element connections[i] = [ui, vi]
    indicates a connection between station ui and station vi. Stations that are
    directly or indirectly connected form a power grid.

    Initially, all stations are online (operational).

    Given a 2D array queries, where each query is one of the following two
    types:
    * [1, x]: A maintenance check is requested for station x. If station x is
      online, it resolves the check by itself. If station x is offline, the
      check is resolved by the operational station with the smallest id in the
      same power grid as x. If no operational station exists in that grid,
      return -1.
    * [2, x]: Station x goes offline (ie it becomes non-operational).

    Return an array of integers representing the results of each query of type
    [1, x] in the order they appear.

    Note: The power grid preserves its structure, an offline (non-operational)
    node remains part of its grid and taking it offline does not alter
    connectivity.
    '''
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        grids = defaultdict(SortedSet)
        powerGrid = [-1] * (c + 1)
        graph = {i:set() for i in range(1,c+1)}
        for u,v in connections:
            graph[u].add(v)
            graph[v].add(u)
        def dfs(node:int, last:int, grid:int) -> None:
            if powerGrid[node] != -1:
                return
            powerGrid[node] = grid
            grids[grid].add(node)
            for next in graph[node]:
                if next != last:
                    dfs(next, node, grid)
        for i in range(1,c+1):
            if powerGrid[i] != -1:
                continue
            dfs(i, -1, len(grids) + 1)
        answer = []
        for op, node in queries:
            g = powerGrid[node]
            if op == 2:
                if node in grids[g]:
                    grids[g].remove(node)
            elif node in grids[g]:
                answer.append(node)
            elif len(grids[g]) > 0:
                answer.append(grids[g][0])
            else:
                answer.append(-1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [[1,2],[2,3],[3,4],[4,5]]
        k = [[1,3],[2,1],[1,1],[2,2],[1,2]]
        o = [3,2,3]
        self.assertEqual(s.processQueries(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = []
        k = [[1,1],[2,1],[1,1]]
        o = [1,-1]
        self.assertEqual(s.processQueries(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [[3,2],[1,3],[2,1]]
        k = [[2,1]]
        o = []
        self.assertEqual(s.processQueries(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)