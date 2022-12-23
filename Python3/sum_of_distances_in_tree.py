# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import collections
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is an undirected connected tree with n nodes labeled from 0 to n - 1
    and n - 1 edges.

    Given the integer n and the array edges where edges[i] = [ai, bi] indicates
    that there is an edge between nodes ai and bi in the tree.

    Return an array answer of length n where answer[i] is the sum of the
    distances between the ith node in the tree and all other nodes.
    '''
    def sumOfDistancesInTree_brute(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        def bfs(start,target):
            if start == target:
                return 0
            visited = set()
            queue = deque([(start,0)])
            while queue:
                current, distance = queue.popleft()
                if current in visited:
                    continue
                if current == target:
                    return distance
                visited.add(current)
                for i in graph[current]:
                    queue.append((i, distance + 1))
            return n
        dp = [[bfs(i,j) for j in range(n)] for i in range(n)]
        return [sum(i) for i in dp]

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        dp = [[n] * n for _ in range(n)]
        def bfs(start,target):
            if start == target:
                return 0
            visited = set()
            queue = deque([(start,0)])
            while queue:
                current, distance = queue.popleft()
                if current in visited:
                    continue
                if current == target:
                    return distance
                visited.add(current)
                for i in graph[current]:
                    # what else do with this dp``
                    dp[current][i] = distance + 1
                    queue.append((i, distance + 1))
            return n
        for i in range(n):
            for j in range(n):
                dp[i][j] = bfs(i,j)
        return [sum(i) for i in dp]

    def sumOfDistancesInTree_leetcode(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N
        def dfs(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 6
        j = [[0,1],[0,2],[2,3],[2,4],[2,5]]
        o = [8,12,6,10,10,10]
        self.assertEqual(s.sumOfDistancesInTree(i,j), o)

    def test_two(self):
        s = Solution()
        i = 1
        j = []
        o = [0]
        self.assertEqual(s.sumOfDistancesInTree(i,j), o)

    def test_three(self):
        s = Solution()
        i = 2
        j = [[1,0]]
        o = [1,1]
        self.assertEqual(s.sumOfDistancesInTree(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)