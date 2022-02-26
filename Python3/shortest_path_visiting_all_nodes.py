# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an undirected, connected graph of n nodes labeled 0 to n-1
    represented by an array graph where graph[i] is a list of all the
    nodes connected with node i by an edge.

    Return the length of the shortest path that visits every node. It is
    possible to start and stop at any node, nodes may be revisited 
    multiple times, and edges may be used multiple times.

    Constraints:
    * 1 <= n <= 12 (ie max of 12 nodes)
    * 0 <= graph[i].length < n (ie nodes have 0 to 11 edges)
    * node cannot have edge to itself
    '''
    # got frustrated and read the solution and based implementation on it
    # https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/
    # DFS (dynamic programing caching) with bitmasking to record state
    # O(2^N N^2) time (2^N possible states for N nodes run N times)
    # O(2^N N) space (total possible states in cache)
    def shortestPathLength_dfs(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # node, bitmask -> distance
        cache = dict()
        # dynamic programming depth first search
        def dp_dfs(node, mask):
            state = (node, mask)
            # check cache for quick answer
            if state in cache:
                return cache[state]
            # check for base case (only one node visited [ie start node])
            # make use of Brian Kernighan's method
            if (mask & (mask - 1)) == 0:
                return 0
            # add state to cache (with large value to avoid infinite cycles)
            cache[state] = float('inf')
            # update state to have smallest value for all neighbors
            for e in graph[node]:
                # because removing nodes from mask make sure neighbor can be removed
                # this is because top down ((start) '1111' -> '1011' -> ... -> '1000' (base))
                if mask & (1 << e):
                    cache[state] = min(
                        cache[state],
                        1 + dp_dfs(e, mask), # already visited
                        1 + dp_dfs(e, mask ^ (1 << node)) # fist visit
                    )
            # return best distance for this state
            return cache[state]
        # return smallest distance with start node touching all nodes
        return min(dp_dfs(i, (1 << n) - 1) for i in range(n))

    # again based on leetcode algorithm explanation
    # https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/
    # same time/space as dfs but likely to return early
    def shortestPathLength_bfs(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # only one node in graph
        if n == 1:
            return 0
        emask = (1 << n) - 1
        visited = {(i, 1 << i) for i in range(n)}
        queue = [(i, 1 << i) for i in range(n)]
        distance = 0
        while queue:
            nextQueue = []
            for node, mask in queue:
                for e in graph[node]:
                    newMask = mask | (1 << e)
                    if newMask == emask:
                        return 1 + distance
                    state = (e, newMask)
                    if state not in visited:
                        visited.add(state)
                        nextQueue.append(state)
            distance += 1
            queue = nextQueue

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[0],[0],[0]]
        o = 4
        self.assertEqual(s.shortestPathLength_dfs(i), o)
        self.assertEqual(s.shortestPathLength_bfs(i), o)

    def test_two(self):
        s = Solution()
        i = [[1],[0,2,4],[1,3,4],[2],[1,2]]
        o = 4
        self.assertEqual(s.shortestPathLength_dfs(i), o)
        self.assertEqual(s.shortestPathLength_bfs(i), o)

    def test_three(self):
        s = Solution()
        i = [[1],[0]]
        o = 1
        self.assertEqual(s.shortestPathLength_dfs(i), o)
        self.assertEqual(s.shortestPathLength_bfs(i), o)

    def test_four(self):
        s = Solution()
        i = [[1],[0,2],[1]]
        o = 2
        self.assertEqual(s.shortestPathLength_dfs(i), o)
        self.assertEqual(s.shortestPathLength_bfs(i), o)

    def test_five(self):
        s = Solution()
        i = [[]]
        o = 0
        self.assertEqual(s.shortestPathLength_dfs(i), o)
        self.assertEqual(s.shortestPathLength_bfs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)