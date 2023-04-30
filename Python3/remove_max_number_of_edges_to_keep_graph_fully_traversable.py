# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class UnionFind:
    # Initialize the list representative and componentSize
    # Each node is a representative of itself with size 1.
    def __init__(self, n:int) -> None:
        self.representative = list(range(n+1))
        self.componentSize = [1] * (n+1)
        self.components = n

    # Get the root of a node.
    def findRepresentative(self, x:int) -> int:
        if self.representative[x] == x:
            return x
        # path compression
        self.representative[x] = self.findRepresentative(self.representative[x])
        return self.representative[x]

    # Perform union of two components that belong to node x and node y
    def performUnion(self, x:int, y:int) -> int:
        x = self.findRepresentative(x)
        y = self.findRepresentative(y)

        if x == y:
            return 0
        
        if self.componentSize[x] > self.componentSize[y]:
            self.componentSize[x] += self.componentSize[y]
            self.representative[y] = x
        else:
            self.componentSize[y] += self.componentSize[x]
            self.representative[x] = y
        
        self.components -= 1
        return 1
    
    # Returns true if all nodes get merged to one.
    def isConnected(self) -> bool:
        return self.components == 1

class Solution:
    '''
    Alice and Bob have an undirected graph of n nodes and three types of edges:
    * Type 1: Can be traversed by Alice only.
    * Type 2: Can be traversed by Bob only.
    * Type 3: Can be traversed by both Alice and Bob.

    Given an array edges where edges[i] = [typei, ui, vi] represents a
    bidirectional edge of type typei between nodes ui and vi, find the maximum
    number of edges that can be removed such that after removing the edges the
    graph can still be fully traversed by both Alice and Bob. The graph is fully
    traversed by Alice and Bob if starting from any node, they can reach all
    other nodes.

    Return the maximum number of edges that can be removed, or -1 if Alice and
    Bob cannot fully traverse the graph.
    '''
    # disjoint set union based on editorial by leetcode
    # https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/editorial/
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)

        edgesRequired = 0

        # perform union for type 3 edges on alice and bob 
        for i,j,k in edges:
            if i == 3:
                edgesRequired += alice.performUnion(j,k) | bob.performUnion(j,k)
        
        # perform union for alice if type 1 and for bob if type 2
        for i,j,k in edges:
            if i == 1:
                edgesRequired += alice.performUnion(j,k)
            elif i == 2:
                edgesRequired += bob.performUnion(j,k)
        
        # check if graph alice and bob have n-1 edges or is single component
        if alice.isConnected() and bob.isConnected():
            return len(edges) - edgesRequired
        
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
        o = 2
        self.assertEqual(s.maxNumEdgesToRemove(i,j), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
        o = 0
        self.assertEqual(s.maxNumEdgesToRemove(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = [[3,2,3],[1,1,2],[2,3,4]]
        o = -1
        self.assertEqual(s.maxNumEdgesToRemove(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)