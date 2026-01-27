# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a directed weighted graph with n nodes labeled from 0 to n - 1, and an
    array edges where edges[i] = [ui, vi, wi] represents a directed edge from
    node ui to node vi with weight wi.

    Each node ui has a switch that can be used at most once: when arriving at ui
    and the switch not yet been activated, it is possible to activate the switch
    on one of its incoming edges vi -> ui to reverse that edge to ui -> vi and
    immediately traverse it.

    The reversal is only valid for that single move, and using a reversed edge
    costs 2 * wi.

    Return the minimum total cost to travel from node 0 to node n-1. If it is
    not possible, return -1. 
    '''
    # based on hints
    # observation in shortest path, nodes are traversed at most once, so just
    # the reversed edges to graph and use Dijkstra.
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(dict)
        def add(u,v,w):
            if v in graph[u]:
                graph[u][v] = min(w, graph[u][v])
            else:
                graph[u][v] = w
        for u,v,w in edges:
            add(u,v,w)
            add(v,u,2*w)
        queue = [(0,0)]
        visited = set()
        while queue:
            answer, node = heapq.heappop(queue)
            if node in visited:
                continue
            if node == n-1:
                return answer
            visited.add(node)
            for x in graph[node]:
                if x not in visited:
                    heapq.heappush(queue, (answer + graph[node][x], x))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
        o = 5
        self.assertEqual(s.minCost(i,j), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]
        o = 3
        self.assertEqual(s.minCost(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)