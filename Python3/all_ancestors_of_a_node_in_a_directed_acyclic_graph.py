# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n representing the number of nodes in a directed
    acyclic graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

    Also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes
    that there is a unidirectional edge from fromi to toi in the graph.

    Return a list answer, where answer[i] is the list of ancestors of the ith
    node, sorted in ascending order.

    A node u is an ancestor of another node v if u can reach v via a set of
    edges.
    '''
    # bad logic (maybe...)
    def getAncestors_wrong(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i:[set(),set()] for i in range(n)}
        for i,j in edges:
            graph[i][0].add(j)
        process = deque([i for i in graph if len(graph[i][0]) == 1])
        while process:
            p = process.popleft()
            for e in graph[p][0]:
                if p in graph[e][0]:
                    graph[e][0].remove(p)
                graph[e][1].add(p)
                if len(graph[e][0]) == 1:
                    process.append(e)
        return [sorted(graph[i][1]) for i in range(n)]

    # brute force -> time limit exceeded
    def getAncestors_tle(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i:[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
        answer = [set() for i in range(n)]
        def dfs(i:int, j:int):
            if i != j:
                answer[i].add(j)
            for e in graph[i]:
                dfs(e, j)
        for i in range(n):
            dfs(i,i)
        return [sorted(i) for i in answer]

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i:set() for i in range(n)}
        for i,j in edges:
            graph[j].add(i)
        @cache
        def dfs(i:int) -> Set[int]:
            s = set(graph[i])
            pass
            for j in graph[i]:
                s.update(dfs(j))
            return s
        return [sorted(dfs(i)) for i in range(n)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 8
        j = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
        o = [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
        self.assertEqual(s.getAncestors(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        o = [[],[0],[0,1],[0,1,2],[0,1,2,3]]
        self.assertEqual(s.getAncestors(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)