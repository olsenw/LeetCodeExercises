# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer k and the following arrays:
    * a 2D integer array rowConditions of size n where
      rowConditions[i] = [abovei, belowi].
    * a 2D integer array colConditions of size m where
      colConditions[i] = [lefti, righti]
    
    The two arrays contain integers from 1 to k.

    Build a k x k matrix that contains each of the numbers from 1 to k exactly
    once. The remaining cells should have the value 0.

    The matrix should also satisfy the following conditions:
    * The number abovei should appear in a row that is strictly above the row at
      which the number belowi appears for all i from 0 to n - 1.
    * The number lefti should appear in a column that is strictly left of the
      column at which the number righti appears for all i from 0 to m - 1.

    Return any matrix that satisfies the conditions. If no answer exists return
    an empty matrix.
    '''
    def buildMatrix_(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        m = len(colConditions)
        n = len(rowConditions)
        # node -> left, right, up, down
        graph = {i:[set(),set(),set(),set()] for i in range(1,k+1)}
        for i,j in rowConditions:
            graph[i][0].add(j)
            graph[j][1].add(i)
        for i,j in colConditions:
            graph[i][2].add(j)
            graph[j][3].add(i)
        graph = {i:[sorted(j) for j in graph[i]] for i in range(1,k+1)}
        return

    # based on leetcode dfs solution
    # https://leetcode.com/problems/build-a-matrix-with-conditions/?envType=daily-question&envId=2024-07-21
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(node, graph, visited, order, cycle):
            visited[node] = 1
            for i in graph[node]:
                if visited[i] == 0:
                    dfs(i, graph, visited, order, cycle)
                    if cycle[0]:
                        return
                elif visited[i] == 1:
                    cycle[0] = True
                    return
            visited[node] = 2
            order.append(node)
            return 
        def topoSort(conditions, n):
            adj = defaultdict(list)
            for i,j in conditions:
                adj[i].append(j)
            visited = [0] * (n+1)
            order = []
            cycle = [False] # this is important for pointer passing
            for i in range(1,n+1):
                if visited[i] == 0:
                    dfs(i, adj, visited, order, cycle)
                    if cycle[0]:
                        return []
            return order[::-1]
        rowOrder = topoSort(rowConditions, k)
        if len(rowOrder) == 0:
            return []
        colOrder = topoSort(colConditions, k)
        if len(colOrder) == 0:
            return []
        answer = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if rowOrder[i] == colOrder[j]:
                    answer[i][j] = rowOrder[i]
        return answer
        # return [[rowOrder[i] if rowOrder[i] == colOrder[j] else 0 for j in range(k)] for i in range(k)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[1,2],[3,2]]
        k = [[2,1],[3,2]]
        o = [[3,0,0],[0,0,1],[0,2,0]]
        self.assertEqual(s.buildMatrix(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[1,2],[2,3],[3,1],[2,3]]
        k = [[2,1]]
        o = []
        self.assertEqual(s.buildMatrix(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)