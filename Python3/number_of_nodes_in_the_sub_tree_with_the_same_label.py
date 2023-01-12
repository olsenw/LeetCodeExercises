# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a tree (ie a connected, undirected graph that has no cycles)
    consisting of n nodes numbered from 0 to n - 1 and exactly n-1 edges. The
    root of the tree is the node 0, and each node of the tree has a label which
    is a lower-case character given in the string labels (ie the node with the
    number i has the label labels[i]).

    The edges array is given on the form edges[i] = [ai, bi], which means there
    is an edge between nodes ai and bi in the tree.

    Return an array of size n where ans[i] is the number of nodes in the subtree
    of the ith node which have the same label as node i.

    A subtree of tree T is the tree consisting of a node in T and all of its
    descendant nodes.
    '''
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        g = {i:[] for i in range(n)}
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        v = set()
        def dfs(i):
            c = Counter()
            v.add(i)
            for e in g[i]:
                if e not in v:
                    c += dfs(e)
            c[labels[i]] += 1
            ans[i] = c[labels[i]]
            return c
        dfs(0)
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 7
        j = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
        k = "abaedcd"
        o = [2,1,1,1,1,1,1]
        self.assertEqual(s.countSubTrees(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [[0,1],[1,2],[0,3]]
        k = "bbbb"
        o = [4,2,1,1]
        self.assertEqual(s.countSubTrees(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 5
        j = [[0,1],[0,2],[1,3],[0,4]]
        k = "aabab"
        o = [3,2,1,1,1]
        self.assertEqual(s.countSubTrees(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)