# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n representing the number of nodes in a directed weighted
    graph, numbered from 0 to n - 1. This is represented by a 2D integer array
    edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui
    to node vi with weight wi.

    Also given a string labels of length n, where labels[i] is the character
    assigned to node i, and an integer k.

    Return the minimum total edge weight of a path from node 0 to node n - 1
    such that the concatenation of the labels of the nodes along the path
    contains at most k consecutive identical characters. If no valid path
    exists, return -1.
    '''
    def shortestPath_fails_cycles(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = {i:{} for i in range(n)}
        totalWeight = 1
        for u,v,w in edges:
            graph[u][v] = w
            totalWeight += w
        route = []
        def dfs(node:int, weight:int) -> int:
            route.append(labels[node])
            if len(route) > k and all(route[i] == route[-1] for i in range(-1,-k-2,-1)):
                route.pop()
                return -1
            if node == n-1:
                route.pop()
                return weight
            answer = float('inf')
            for i in graph[node]:
                j = dfs(i, weight + graph[node][i])
                if j > -1:
                    answer = min(answer, j)
            route.pop()
            return answer if answer < totalWeight else -1
        return dfs(0,0)

    # https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/
    def shortestPath_fails(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = {i:{} for i in range(n)}
        totalWeight = 1
        for u,v,w in edges:
            if v not in graph[u]:
                graph[u][v] = w
            else:
                graph[u][v] = min(graph[u][v], w)
            totalWeight += w
        distance = [totalWeight] * n
        distance[0] = 0
        queue = [(0,1,0)] # (distance, count, node)
        while queue:
            dist, count, node = heapq.heappop(queue)
            if dist > distance[node]:
                continue
            if count > k:
                continue
            for i in graph[node]:
                d = dist + graph[node][i]
                c = 1 if labels[i] != labels[node] else count + 1
                if d < distance[i] and c <= k:
                    distance[i] = d
                    heapq.heappush(queue, (d,c,i))
        return distance[-1] if distance[-1] < totalWeight else -1

    # based on Leedcode editorial
    # https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/editorial/?envType=daily-question&envId=2026-10-30
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = {i:{} for i in range(n)}
        totalWeight = 1
        for u,v,w in edges:
            if v not in graph[u]:
                graph[u][v] = w
            else:
                graph[u][v] = min(graph[u][v], w)
            totalWeight += w
        distance = [[totalWeight] * (k+1) for _ in range(n)]
        distance[0][1] = 0
        # (distance, node, consecutive letter count)
        queue = []
        heapq.heappush(queue, (0,0,1))
        while queue:
            dist, node, count = heapq.heappop(queue)
            if dist > distance[node][count]:
                continue
            if node == n - 1:
                return dist
            for i in graph[node]:
                c = 1 if labels[i] != labels[node] else count + 1
                if c > k:
                    continue
                d = dist + graph[node][i]
                if d < distance[i][c]:
                    distance[i][c] = d
                    heapq.heappush(queue, (d,i,c))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[0,1,1],[1,2,1],[0,2,3]]
        k = "aab"
        l = 1
        o = 3
        self.assertEqual(s.shortestPath(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[0,1,1],[1,2,1],[0,2,3]]
        k = "aab"
        l = 2
        o = 2
        self.assertEqual(s.shortestPath(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [[0,1,1],[1,2,1]]
        k = "aaa"
        l = 2
        o = -1
        self.assertEqual(s.shortestPath(i,j,k,l), o)

    def test_four(self):
        s = Solution()
        i = 5
        j = [[2,0,3632],[2,0,6106],[4,2,9001],[2,1,6743],[0,1,6],[1,2,4],[2,3,1],[3,4,3]]
        k = "ababa"
        l = 2
        o = 14
        self.assertEqual(s.shortestPath(i,j,k,l), o)

    def test_five(self):
        s = Solution()
        i = 10
        # j = [[0,5,28],[0,1,5052],[0,5,5849],[8,9,6454],[1,3,3715],[0,9,1328],[5,1,688],[6,5,9937],[9,3,8164],[0,1,3],[1,2,3],[2,3,10],[3,4,7],[4,5,6],[5,6,4],[6,7,1],[7,8,10],[8,9,5]]
        j = [[0,5,28],[0,1,3],[1,2,3],[2,3,10],[3,4,7],[4,5,6],[5,6,4],[6,7,1],[7,8,10],[8,9,5]]
        k = "ababababab"
        #    0123456789
        l = 3
        o = 48
        self.assertEqual(s.shortestPath(i,j,k,l), o)

    def test_six(self):
        s = Solution()
        i = 10
        j = [[0,5,28],[0,1,5052],[0,5,5849],[8,9,6454],[1,3,3715],[0,9,1328],[5,1,688],[6,5,9937],[9,3,8164],[0,1,3],[1,2,3],[2,3,10],[3,4,7],[4,5,6],[5,6,4],[6,7,1],[7,8,10],[8,9,5]]
        # j = [[0,5,28],[0,1,3],[1,2,3],[2,3,10],[3,4,7],[4,5,6],[5,6,4],[6,7,1],[7,8,10],[8,9,5]]
        k = "ababababab"
        #    0123456789
        l = 3
        o = 48
        self.assertEqual(s.shortestPath(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)