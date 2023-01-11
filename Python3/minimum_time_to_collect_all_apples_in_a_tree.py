# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an undirected tree consisting of n vertices numbered from 0 to n-1,
    which has some apples in their vertices. It takes one second to traverse an
    edge. Return the minimum time in seconds to collect all apples in the tree,
    while starting and ending at vertex 0.

    The edges of the undirected tree are given in the array edges, where
    edges[i] = [ai, bi] means there exists an edge connecting the vertices ai
    and bi. Additionally, there is a boolean array hasApple, where
    hasApple[i] = true means that the vertex i has an apple; otherwise it does
    not have any apple.
    '''
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = {i:[] for i in range(n)}
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        v = set()
        def dfs(i):
            v.add(i)
            c = 0
            for e in g[i]:
                if e not in v:
                    c += dfs(e)
            v.remove(i)
            return c + 2 if c or hasApple[i] else 0
        a = dfs(0)
        return a - 2 if a else 0 

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 7
        j = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
        k = [False,False,True,False,True,True,False]
        o = 8
        self.assertEqual(s.minTime(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 7
        j = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
        k = [False,False,True,False,True,True,False]
        o = 8
        self.assertEqual(s.minTime(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 7
        j = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
        k = [False,False,False,False,False,False,False]
        o = 0
        self.assertEqual(s.minTime(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 4
        j = [[0,2],[0,3],[1,2]]
        k = [False,True,False,False]
        o = 4
        self.assertEqual(s.minTime(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)