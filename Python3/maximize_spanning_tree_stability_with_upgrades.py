# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, representing n nodes numbered from 0 to n-1 and a list
    of edges, where edges[i] = [ui, vi, si, musti]:
    * ui and vi indicates an undirected edge between nodes ui and vi.
    * si is the strength of the edge.
    * musti is an integer (0 or 1). If musti == 1, the edge must be included in
      the spanning tree. These edges cannot be upgraded.
    
    Also given an integer k, the maximum number of upgrades that can be
    preformed. Each upgrade doubles the strength of an edge, and each eligible
    edge (with musti == 0) can be upgraded at most once.

    The stability of a spanning tree is defined as the minimum strength score
    among all edges included in it.

    Return the maximum possible stability of any valid spanning tree. If it is
    impossible to connect all nodes, return -1.

    Note: A spanning tree of a graph with n nodes is a subset of the edges that
    connects all nodes together (ie the graph is connected) without forming any
    cycles, and uses exactly n - 1 edges.
    '''
    # based on Leetcode editorial
    # https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/editorial/?envType=daily-question&envId=2026-03-12
    # use binary search on possible answer  range (0 -> minimum weight of required edges)
    # use a function to test building a spanning tree only using edges with given weight
    # this is done with Kruskal's algorithm (makes use of spanning trees)
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        class DSU:
            def __init__(self, parent):
                self.parent = parent
            def find(self, x):
                if self.parent[x] == x:
                    return x
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            def join(self, x, y):
                px = self.find(x)
                py = self.find(y)
                self.parent[px] = py

        # base case where too few edges to form a spanning tree
        if len(edges) < n - 1:
            return -1
        
        # edges that must be included in the spanning tree
        requiredEdges = [e for e in edges if e[3] == 1]
        # edges that could be included in spanning tree
        optionalEdges = [e for e in edges if e[3] == 0]
        optionalEdges.sort(reverse=True, key=lambda x:x[2])

        # create initial union find based on required edges
        selectedInitial = 0
        requiredMinStability = 2 * 10**5 # derived from problem constraints
        dsuInitial = DSU(list(range(n)))

        for i,j,s,_ in requiredEdges:
            if dsuInitial.find(i) == dsuInitial.find(j) or selectedInitial == n - 1:
                return -1
            dsuInitial.join(i,j)
            selectedInitial += 1
            requiredMinStability = min(requiredMinStability, s)

        # check if possible to build spanning tree with minimum weight
        def test(weight:int) -> bool:
            dsu = DSU(dsuInitial.parent[:])
            selected = selectedInitial
            doubledCount = 0
            for i,j,s,_ in optionalEdges:
                if dsu.find(i) == dsu.find(j):
                    continue
                # greedy add largest weight edge
                if s >= weight:
                    dsu.join(i,j)
                    selected += 1
                # if double edge works, greedy add it
                elif doubledCount < k and s * 2 >= weight:
                    doubledCount += 1
                    dsu.join(i,j)
                    selected += 1
                # unable to add additional edges... probably failed making span
                else:
                    break
                # conditions met for a spanning tree
                if selected == n - 1:
                    break
            # valid spanning tree if selected n-1 edges
            return selected != n - 1
        # binary search on answer
        i = 0
        j = requiredMinStability
        while i < j:
            # mid = (i + j) // 2
            mid = i + (j-i+1) // 2
            if test(mid):
                j = mid - 1
            else:
                i = mid
        # if i is 0, means no binary search for answer was run
        # if valid answer minimum possible i is 1 by problem constraints
        return i if i > 0 else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[0,1,2,1],[1,2,3,0]]
        k = 1
        o = 2
        self.assertEqual(s.maxStability(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[0,1,4,0],[1,2,3,0],[0,2,1,0]]
        k = 2
        o = 6
        self.assertEqual(s.maxStability(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [[0,1,1,1],[1,2,1,1],[2,0,1,1]]
        k = 0
        o = -1
        self.assertEqual(s.maxStability(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 10
        j = [[1,3,85282,1],[2,7,15170,1],[5,8,83816,0],[0,9,6574,1],[0,6,97906,0],[7,9,3,0],[8,9,87261,1],[3,9,21740,0],[2,6,90270,0],[3,6,47414,1],[6,9,57119,0],[7,8,46995,0]]
        k = 7
        o = -1
        self.assertEqual(s.maxStability(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)