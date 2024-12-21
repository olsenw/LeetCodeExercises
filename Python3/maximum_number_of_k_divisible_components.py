# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an undirected tree with n nodes labeled from 0 to n - 1. Given an
    integer n and a 2D integer array edges of length n - 1, where
    edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi
    in the tree.

    Also given a 0-indexed integer array values of length n, where values[i] is
    the value associated with the ith node, and an integer k.

    A valid split of the tree is obtained by removing any set of edges, possibly
    empty, from the tree such that the resulting components all have values that
    are divisible ny k, where the value ofa connected component is the sum of
    the values of its nodes.

    Return the maximum number of components in any valid split.
    '''
    # based on hints (give away the process)
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = {i:set() for i in range(n)}
        graph[-1] = {0}
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        visited = {-1}
        answer = 0
        def dfs(node):
            nonlocal answer
            visited.add(node)
            for i in graph[node]:
                if i in visited:
                    continue
                values[node] += dfs(i)
            if values[node] % k:
                return values[node]
            answer += 1
            return 0
        dfs(0)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [[0,2],[1,2],[1,3],[2,4]]
        k = [1,8,1,4,4]
        l = 6
        o = 2
        self.assertEqual(s.maxKDivisibleComponents(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 7
        j = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
        k = [3,0,6,1,5,2,1]
        l = 3
        o = 3
        self.assertEqual(s.maxKDivisibleComponents(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = []
        k = [5]
        l = 5
        o = 1
        self.assertEqual(s.maxKDivisibleComponents(i,j,k,l), o)

    def test_four(self):
        s = Solution()
        i = 2
        j = [[0,1]]
        k = [5,3]
        l = 4
        o = 1
        self.assertEqual(s.maxKDivisibleComponents(i,j,k,l), o)

    def test_five(self):
        s = Solution()
        i = 2
        j = [[0,1]]
        k = [8,4]
        l = 4
        o = 2
        self.assertEqual(s.maxKDivisibleComponents(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)