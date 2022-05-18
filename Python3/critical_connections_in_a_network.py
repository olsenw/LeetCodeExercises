# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are n servers numbered 0 to n - 1 connected by undirected
    server-to-server connections forming a network where
    connections[i] = [ai, bi] represents a connection between servers
    ai and bi. Any server can reach other servers directly or indirectly
    through the network.

    A critical connection is a connection that, if removed, will make
    some servers unable to reach some other server.

    Return all critical connections in the network in any order.
    '''
    
    # based on discussion post by sgallivan
    # https://leetcode.com/problems/critical-connections-in-a-network/discuss/1174196/JS-Python-Java-C%2B%2B-or-Tarjan's-Algorithm-Solution-w-Explanation
    # makes use of Tarjan's Bridge-Finding Algorithm
    def dfs(self, c, p):
        self.visited[c] = self.time
        self.low[c] = self.time
        self.time += 1
        for n in self.graph[c]:
            if not self.visited[n]:
                self.dfs(n, c)
                self.low[c] = min(self.low[c], self.low[n])
            elif n != p:
                self.low[c] = min(self.low[c], self.visited[n])
            if self.low[n] > self.visited[c]:
                self.ans.append([c,n])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.graph = {i:[] for i in range(n)}
        for i,j in connections:
            self.graph[i].append(j)
            self.graph[j].append(i)
        self.visited = [0] * n
        self.low = [0] * n
        self.time = 1
        self.ans = []
        self.dfs(0, -1)
        return self.ans

    '''
    Below is my initial attempt to solve this... did not understand what
    was going on and could only find the vertices that formed the
    biconnected components.
    '''
    # Biconnected component algorithm (John Hopcroft and Robert Tarjan)
    # https://en.wikipedia.org/wiki/Biconnected_component
    # This only returns (in self.articulation) vertices that the graph
    # would need to be divided at to create biconnected components.
    def getArticulationPoints(self, i, d):
        self.visited[i] = True
        self.depth[i] = d
        self.low[i] = d
        children = 0
        articulation = False
        for n in self.graph[i]:
            if not self.visited[n]:
                self.parent[n] = i
                self.getArticulationPoints(n, d + 1)
                children += 1
                if self.low[n] >= self.depth[i]:
                    articulation = True
                self.low[i] = min(self.low[i], self.low[n])
            elif n != self.parent[i]:
                self.low[i] = min(self.low[i], self.depth[n])
        
        if (self.parent[i] and articulation) or (not self.parent[i] and children > 1):
            self.articulation.append(i)

    def criticalConnections_incomplete(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.graph = {i:[] for i in range(n)}
        for i,j in connections:
            self.graph[i].append(j)
            self.graph[j].append(i)
        self.articulation = []
        self.visited = [False] * n
        self.depth = [0] * n
        self.low = [0] * n
        self.parent = [None] * n
        self.getArticulationPoints(0, 0)
        return self.articulation

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [[0,1],[1,2],[2,0],[1,3]]
        o = [[1,3]]
        self.assertEqual(s.criticalConnections(i, j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [[0,1]]
        o = [[0,1]]
        self.assertEqual(s.criticalConnections(i, j), o)

    def test_three(self):
        s = Solution()
        i = 10
        j = [[0,1],[1,2],[2,0],[2,3],[3,4],[4,5],[5,3],[4,6],[5,7],[2,8],[2,9]]
        o = [[5,7],[4,6],[2,3],[2,8],[2,9]]
        self.assertEqual(s.criticalConnections(i, j), o)

    def test_four(self):
        s = Solution()
        i = 3
        j = [[0,1],[1,2],[2,0]]
        o = []
        self.assertEqual(s.criticalConnections(i, j), o)

    def test_five(self):
        s = Solution()
        i = 3
        j = [[0,1],[0,2]]
        o = [[0,1],[0,2]]
        self.assertEqual(s.criticalConnections(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)