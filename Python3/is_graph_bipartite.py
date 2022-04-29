# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is an undirected graph with n nodes, where each node is
    numbered between 0 and n - 1. Given a 2D array graph where graph[u]
    is an array of nodes that node u is adjacent to. More formally, for
    each v in graph[u] there is an undirected edge between node u and
    node v. The graph has the following properties:
    * There are no self-edges (graph[u] does not contain u).
    * There are no parallel edges (graph[u] does not contain duplicate
      values).
    * If v is in graph[u], the u is in graph[v] (the graph is 
      undirected).
    * The graph may not be connected meaning there may be two nodes u
      and v such that there is no path between them.
    
    A graph is bipartite if the nodes can be partitioned into two
    independent sets A and B such that every edge in the graph connects
    a node in set A with a node in set B.

    Return True if and only if the graph is bipartite.
    '''
    def isBipartite(self, graph: List[List[int]]) -> bool:
        v = [False] * len(graph)
        a = set()
        b = set()
        # go over all nodes (in case of unconnected graph)
        for n in range(len(graph)):
            # no need to revisit nodes
            if not v[n]:
                v[n] = True
                a.add(n)
                nodes = graph[n]
                while nodes:
                    new = set()
                    for i in nodes:
                        # connects in set preventing bipartite
                        if i in a:
                            return False
                        # no need to revisit nodes
                        if not v[i]:
                            v[i] = True
                            b.add(i)
                            for e in graph[i]:
                                # connects in set preventing bipartite
                                if e in b:
                                    return False
                                new.add(e)
                    nodes = new
                    a, b = b, a
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[0,2],[0,1,3],[0,2]]
        o = False
        self.assertEqual(s.isBipartite(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,3],[0,2],[1,3],[0,2]]
        o = True
        self.assertEqual(s.isBipartite(i), o)

    def test_three(self):
        s = Solution()
        i = [[]]
        o = True
        self.assertEqual(s.isBipartite(i), o)

    def test_four(self):
        s = Solution()
        i = [[], []]
        o = True
        self.assertEqual(s.isBipartite(i), o)

    def test_five(self):
        s = Solution()
        i = [[1], [0], [3], [2]]
        o = True
        self.assertEqual(s.isBipartite(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)