# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an undirected tree with n nodes labeled from 1 to n, rooted at node
    1. The tree is represented by a 2D integer array edges of length n-1, where
    edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.

    Initially, all edges have a weight of 0. Assign each edge a weight of 1 or
    2.

    The cost of a path between any two nodes u and v is the total weight of all
    edges in the path connecting them.

    Select any one node x at the maximum depth. Return the number of ways to
    assign edge weights in the path from node 1 to x such that its total cost is
    odd.

    Since the answer may be large return it modulo 10^9 + 7.

    Note: Ignore all edges not in the path from node 1 to x.
    '''
    # invalid dp relation
    def assignEdgeWeights_fails(self, edges: List[List[int]]) -> int:
        m = 10**9+7
        tree = defaultdict(list)
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        def dfs(node:int,parent:int) -> int:
            depth = 0
            for child in tree[node]:
                if child != parent:
                    depth = max(depth, 1 + dfs(child,node))
            return depth
        depth = dfs(1,0)
        def dp(i:int, p:int) -> int:
            if i == depth:
                return p % 2
            return max(1+dp(i+1,(p+1)%2), 1+dp(i+1,(p+2)%2))
        return max(dp(0,0),dp(0,1))

    # draw a picture to show paths and their final edge weights
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        m = 10**9+7
        tree = defaultdict(list)
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        def dfs(node:int,parent:int) -> int:
            depth = 0
            for child in tree[node]:
                if child != parent:
                    depth = max(depth, 1 + dfs(child,node))
            return depth
        depth = dfs(1,0)
        return pow(2, depth-1, m)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2]]
        o = 1
        self.assertEqual(s.assignEdgeWeights(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[1,3],[3,4],[3,5]]
        o = 2
        self.assertEqual(s.assignEdgeWeights(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)