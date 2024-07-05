# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There exist two undirected trees with n and m nodes, numbered from 0 to n-1
    and from 0 to m-1, respectively. Given two 2D integer two 2D integer arrays
    edges1 and edges 2 of lengths n-1 and m-1, respectively, where
    edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi
    in the first tree and edges2[i] = [ui, vi] indicates that there is an edge
    between nodes ui and vi in the second tree.

    Connect one node from the first tree with another node from the second tree
    with an edge.

    Return the minimum possible diameter of the resulting tree.

    The diameter of a tree is the length of the longest path between any two
    nodes in the tree.
    '''
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n, m = len(edges1) + 1, len(edges2) + 1
        a, b = defaultdict(list), defaultdict(list)
        for i,j in edges1:
            a[i].append(j)
            a[j].append(i)
        for i,j in edges2:
            b[i].append(j)
            b[j].append(i)
        @cache
        def adfs(node: int, parent: int) -> int:
            return max((1 + adfs(i, node) for i in a[node] if i != parent), default=0)
        @cache
        def bdfs(node: int, parent: int) -> int:
            return max((1 + bdfs(i, node) for i in b[node] if i != parent), default=0)
        a = list(adfs(i,-1) for i in range(n))
        b = list(bdfs(i,-1) for i in range(m))
        return max(1 + min(a) + min(b), max(a), max(b))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[0,2],[0,3]]
        j = [[0,1]]
        o = 3
        self.assertEqual(s.minimumDiameterAfterMerge(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
        j = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
        o = 5
        self.assertEqual(s.minimumDiameterAfterMerge(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]]
        j = [[0,1],[0,2],[0,3]]
        o = 7
        self.assertEqual(s.minimumDiameterAfterMerge(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)