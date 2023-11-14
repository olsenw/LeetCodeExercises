# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from math import inf
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
based on leetcode solution
Floyd-Warshall algorithm
'''
class Graph:
    # build adjacency matrix
    def __init__(self, n, edges):
        self.n = n
        self.adjacency = [[inf] * n for _ in range(n)]
        for i,j,c in edges:
            self.adjacency[i][j] = c
        for i in range(n):
            self.adjacency[i][i] = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    self.adjacency[j][k] = min(self.adjacency[j][k], self.adjacency[j][i] + self.adjacency[i][k])

    # update adjacency matrix (iterates over whole matrix)
    def addEdge(self, edge:List[int]) -> None:
        x,y,c = edge
        for i in range(self.n):
            for j in range(self.n):
                self.adjacency[i][j] = min(self.adjacency[i][j], self.adjacency[i][x] + self.adjacency[y][j] + c)

    # get pre-computed answer
    def shortestPath(self, node1, node2):
        if self.adjacency[node1][node2] == inf:
            return -1
        return self.adjacency[node1][node2]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
        self.assertEqual(s.shortestPath(3, 2), 6)
        self.assertEqual(s.shortestPath(0, 3), -1)
        s.addEdge([1,3,4])
        self.assertEqual(s.shortestPath(0, 3), 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)