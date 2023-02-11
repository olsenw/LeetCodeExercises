# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set

class Solution:
    '''
    Given an integer n, the number of nodes in a directed graph where the nodes
    are labeled from 0 to n - 1. Each edge is red or blue in this graph, and
    there could be self-edges and parallel edges.

    Given two arrays redEdges and blueEdges where:
    * redEdges[i] = [ai, bi] indicates that there is a directed red edge from
      node ai to node bi in the graph.
    * blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from
      node uj to node vj in the graph.
    
    Return an array answer of length n, where each answer[x] is the length of
    the shortest path from node 0 to node x such that the edge colors alternate
    along the path, or -1 if such a path does not exist.
    '''
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # create graph
        graph: Dict[int,List[Set,Set]] = {i:[set(),set()] for i in range(n)}
        for a,b in redEdges:
            graph[a][0].add(b)
        for a,b in blueEdges:
            graph[a][1].add(b)
        # track best answer
        answer = [-1] * n
        # bfs
        q = deque([(0,'r',0), (0,'b',0)])
        visited: Set[(int, str, int)] = set()
        while q:
            node, color, cost = q.popleft()
            if answer[node] == -1 or cost < answer[node]:
                answer[node] = cost
            # follow blue edges
            if color == 'r':
                for e in graph[node][1]:
                    if (node, 'b', e) not in visited:
                        visited.add((node, 'b', e))
                        q.append((e,'b',cost + 1))
            # follow red edges
            else:
                for e in graph[node][0]:
                    if (node, 'r', e) not in visited:
                        visited.add((node, 'r', e))
                        q.append((e,'r',cost + 1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[0,1],[1,2]]
        k = []
        o = [0,1,-1]
        self.assertEqual(s.shortestAlternatingPaths(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[0,1]]
        k = [[2,1]]
        o = [0,1,-1]
        self.assertEqual(s.shortestAlternatingPaths(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [[0,1],[0,0]]
        k = [[2,1],[0,0]]
        o = [0,1,-1]
        self.assertEqual(s.shortestAlternatingPaths(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)