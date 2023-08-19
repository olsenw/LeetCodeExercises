# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# https://en.wikipedia.org/wiki/Disjoint-set_data_structure
# https://code.activestate.com/recipes/215912-union-find-data-structure/
class DisjointSet:
    def __init__(self) -> None:
        self.weights = {}
        self.parent = {}
        self.objects = {}
        self.nums = {}
    def insertObjects(self, objects):
        for o in objects:
            self.find(o)
    def find(self, object):
        if not object in self.objects:
            n = len(self.objects)
            self.weights[n] = 1
            self.objects[object] = n
            self.nums[n] = object
            self.parent[n] = n
            return object
        s = [self.objects[object]]
        p = self.parent[s[-1]]
        while p != s[-1]:
            s.append(p)
            p = self.parent[p]
        for i in s:
            self.parent[i] = p
        return self.nums[p]
    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap != bp:
            an = self.objects[ap]
            bn = self.objects[bp]
            aw = self.weights[an]
            bw = self.weights[bn]
            if aw < bw:
                ap, bp, an, bn, aw, bw = bp, ap, bn, an, bw, aw
            self.weights[an] = aw + bw
            del self.weights[bn]
            self.parent[bn] = an

class Solution:
    '''
    Given a weighted undirected connected graph with n vertices numbered from 0
    to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a
    bidirectional and weighted edge between nodes ai and bi. A minimum spanning
    tree (MST) is a subset of the graph's edges that connects all vertices
    without cycles and with the minimum possible total edge weight.

    Find all the critical and pseudo-critical edges in the given graph's
    minimum spanning tree (MST). An MST edge whose deletion from the graph would
    cause the MST weight to increase is called a critical edge. In the other
    hand, a pseudo-critical edge is that which can appear in some MSTs but not
    all.

    Note that the indices of the edges in any order.
    '''
    # based on leetcode solution
    # https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/editorial/
    class UnionFind:
        def __init__(self,n) -> None:
            self.parent = list(range(n))
            self.size = [1] * n
            self.maxSize = 1
        def find(self, x):
            # finds the root of x
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self, x, y):
            # connects x and y
            a = self.find(x)
            b = self.find(y)
            if a != b:
                if self.size[a] < self.size[b]:
                    a,b = b,a
                self.parent[b] = a
                self.size[a] += self.size[b]
                self.maxSize = max(self.maxSize, self.size[a])
                return True
            return False
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # sort by edge weight
        indices = sorted(list(range(len(edges))), key=lambda x : edges[x][2])
        # edges required for a minimum MST
        critical = []
        # edges that appear in various minimum MST
        pseudo = []
        # Disjoint set
        u = self.UnionFind(n)
        # minimum MST weight
        weight = 0
        for i in indices:
            a,b,c = edges[i]
            if u.union(a,b):
                weight += c
        # check if edges are critical / pseudo
        for i in indices:
            x,y,z = edges[i]
            # ignore edge and calculate weight
            ignore = self.UnionFind(n)
            ignoreWeight = 0
            for j in indices:
                a,b,c = edges[j]
                if i != j and ignore.union(a,b):
                    ignoreWeight += c
            # if graph is disconnected or total weight is greater the edge
            # is critical
            if ignore.maxSize < n or ignoreWeight > weight:
                critical.append(i)
                continue
            # require the edge and calculate weight
            force = self.UnionFind(n)
            forceWeight = z
            force.union(x,y)
            for j in indices:
                a,b,c = edges[j]
                if i != j and force.union(a,b):
                    forceWeight += c
            # if total weight is same the edge is pseudo
            if forceWeight == weight:
                pseudo.append(i)
        return [critical, pseudo]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
        o = [[0,1],[2,3,4,5]]
        self.assertEqual(s.findCriticalAndPseudoCriticalEdges(i,j), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
        o = [[],[0,1,2,3]]
        self.assertEqual(s.findCriticalAndPseudoCriticalEdges(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)