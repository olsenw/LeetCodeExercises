# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
    find all possible paths from node 0 to node n - 1 and return them in any
    order.

    The graph is given as follows graph[i] is a list of all nodes that can be
    visited from node i (ie, there is a directed edge from node i to node
    graph[i][j]).
    '''
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        n = len(graph) - 1
        queue = deque([[0]])
        while queue:
            p = queue.popleft()
            if p[-1] == n:
                answer.append(p)
                continue
            for i in graph[p[-1]]:
                queue.append(p + [i])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[3],[3],[]]
        o = [[0,1,3],[0,2,3]]
        self.assertEqual(s.allPathsSourceTarget(i), o)

    def test_two(self):
        s = Solution()
        i = [[4,3,1],[3,2,4],[3],[4],[]]
        o = [[0,4],[0,3,4],[0,1,4],[0,1,3,4],[0,1,2,3,4]]
        self.assertEqual(s.allPathsSourceTarget(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)