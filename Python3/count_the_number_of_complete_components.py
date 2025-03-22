# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n. There is an undirected graph with n vertices, numbered
    from 0 to n - 1. Given a 2D integer array edges where edges[i] = [ai, bi]
    denotes that there exists an undirected edge connecting vertices ai and bi.

    Return the number of complete connected components of the graph.

    A connected component is a subgraph of a graph in which there exists a path
    between any two vertices, and no vertex of the subgraph shares an edge with
    a vertex outside of the subgraph.

    A connected component is said to be complete if there exists an edge between
    every pair of its vertices.
    '''
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:set() for i in range(n)}
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        def bfs(node:int) -> Set[int]:
            visited = set()
            queue = deque([node])
            while queue:
                n = queue.popleft()
                if n in visited:
                    continue
                visited.add(n)
                for i in graph[n]:
                    if i not in visited:
                        queue.append(i)
            return visited
        answer = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            v = bfs(i)
            answer += all(len(graph[j]) == len(v) - 1 for j in v)
            visited.update(v)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 6
        j = [[0,1],[0,2],[1,2],[3,4]]
        o = 3
        self.assertEqual(s.countCompleteComponents(i,j), o)

    def test_two(self):
        s = Solution()
        i = 6
        j = [[0,1],[0,2],[1,2],[3,4],[3,5]]
        o = 1
        self.assertEqual(s.countCompleteComponents(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)