# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n teams numbered from 0 to n - 1 in tournament; each team is also
    a node in a DAG.

    Given the integer n and a 0-indexed 2d integer array edges of length m
    representing the DAG, where edges[i] = [ui, vi] indicates that there is a
    directed edge from team ui to team vi in the graph.

    A directed edge from a to b in the graph means that team a is stronger than
    b and team b is weaker than team a.

    Team a will be the champion of the tournament if there is no team b that is
    stronger than team a.

    Return the team that will be the champion of the tournament if there is a
    unique champion, otherwise, return -1.
    '''
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:set() for i in range(n)}
        for a,b in edges:
            graph[b].add(a)
        a = -1
        for i in graph:
            if len(graph[i]) == 0:
                if a != -1:
                    return -1
                a = i
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[0,1],[1,2]]
        o = 0
        self.assertEqual(s.findChampion(i,j), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [[0,2],[1,3],[1,2]]
        o = -1
        self.assertEqual(s.findChampion(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)