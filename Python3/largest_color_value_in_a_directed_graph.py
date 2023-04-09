# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a directed graph of n colored nodes and m edges. The nodes are
    numbered from 0 to n - 1.

    Given a string colors where colors[i] is a lowercase English letter
    representing the color of the ith node in this graph (0-indexed). Also give
    a 2D array edges where edges[j] = [aj, bj] indicates that there is a
    directed edge from node aj to node bj.

    A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk
    such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The
    color value of the path is the number of nodes that are colored the most
    frequently occurring color along that path.

    Return the largest color value of any valid path in the given graph, or -1
    if the graph contains a cycle.
    '''
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        answer = [0] * 26
        graph:Dict[int:List[int,Set]] = {i:[ord(j)-ord('a'),set()] for i,j in enumerate(colors)}
        for i,j in edges:
            graph[i][1].add(j)
        visited = set()
        @cache
        def dfs(n:int) -> List[int]:
            if n in visited:
                raise ValueError("cycle")
            freq = [0] * 26
            visited.add(n)
            for i in graph[n][1]:
                for j,k in enumerate(dfs(i)):
                    freq[j] = max(freq[j],k)
            freq[graph[n][0]] += 1
            visited.remove(n)
            return freq
        # deal with cycles
        try:
            for i in range(len(colors)):
                for j,k in enumerate(dfs(i)):
                    answer[j] = max(answer[j], k)
        except ValueError as err:
            if err.args[0] == "cycle":
                return -1
            raise
        return max(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abaca"
        j = [[0,1],[0,2],[2,3],[3,4]]
        o = 3
        self.assertEqual(s.largestPathValue(i,j), o)

    def test_two(self):
        s = Solution()
        i = "a"
        j = [[0,0]]
        o = -1
        self.assertEqual(s.largestPathValue(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)