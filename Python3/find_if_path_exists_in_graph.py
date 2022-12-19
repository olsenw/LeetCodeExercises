# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a bi-directional graph with n vertices, where each vertex is
    labeled from 0 to n - 1 (inclusive). The edges in the graph are represented
    as a 2D integer array edges, where each edges[i] = (ui, vi) denotes a
    bi-directional edge between vertex ui and vertex vi. Every vertex pair is
    connected by at most one edge, and no vertex has an edge to itself.

    Determine if there is a valid path that exists from vertex source to vertex
    destination.
    '''
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        g = {i:[] for i in range(n)}
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        q = deque([source])
        v = set()
        while q:
            c = q.popleft()
            if c in v:
                continue
            if c == destination:
                return True
            v.add(c)
            for n in g[c]:
                q.append(n)
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[0,1],[1,2],[2,0]]
        k = 0
        l = 2
        o = True
        self.assertEqual(s.validPath(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 6
        j = [[0,1],[0,2],[3,5],[5,4],[4,3]]
        k = 0
        l = 5
        o = False
        self.assertEqual(s.validPath(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = []
        k = 0
        l = 0
        o = True
        self.assertEqual(s.validPath(i,j,k,l), o)

    def test_four(self):
        s = Solution()
        i = 10
        j = [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
        k = 7
        l = 5
        o = True
        self.assertEqual(s.validPath(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)