# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a directed graph of n nodes with each node labeled from 0 to n - 1.
    The graph is represented by a 0-indexed 2D integer array graph where
    graph[i] is an integer array of nodes adjacent to node i, meaning there is
    an edge from node i to each node in graph[i].

    A node is a terminal node if there are no outgoing edges. A node is a safe
    node if every possible path starting from that node leads to a terminal node
    (or another safe node).

    Return an array containing all the safe nodes of the graph. The answer
    should be sorted in ascending order.
    '''
    # based on topological leetcode solution
    # https://leetcode.com/problems/find-eventual-safe-states/editorial/
    # safe nodes are not part of a cycle
    # if node is part of the cycle it will not be traversed
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # how many incoming edges
        indegree = [0] * n
        # incoming edges to node (reverse edges in graph)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in graph[i]:
                adj[j].append(i)
                indegree[i] += 1
        # start bfs on leaf nodes
        q = deque([i for i in range(n) if indegree[i] == 0])
        # safe nodes (no cycles)
        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True
            for neighbor in adj[node]:
                # 'delete' incoming edge
                indegree[neighbor] -= 1
                # if no incoming edges can be treated as leaf
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return [i for i in range(n) if safe[i]]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,3],[5],[0],[5],[],[]]
        o = [2,4,5,6]
        self.assertEqual(s.eventualSafeNodes(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
        o = [4]
        self.assertEqual(s.eventualSafeNodes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)