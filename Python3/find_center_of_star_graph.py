# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an undirected star graph consisting of n nodes labeled from 1 to n.
    A star graph is a graph where there is one center node and exactly n - 1
    edges that connect the center node with every other node.

    Given a 2D integer array edges where each edges[i] = [ui, vi] indicates that
    there is an edge between the nodes ui and vi. Return the center of the given
    star graph.
    '''
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        return max((len(graph[i]), i) for i in graph)[1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,3],[4,2]]
        o = 2
        self.assertEqual(s.findCenter(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[5,1],[1,3],[1,4]]
        o = 1
        self.assertEqual(s.findCenter(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)