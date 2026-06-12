# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an undirected tree with n nodes labeled from 1 to n, rooted at node
    1. The tree is represented by a 2D integer array edges of length n-1, where
    edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi.

    Initially all edges have a weight of 0. Assign each edge a weight of either
    1 or 2.

    The cost of a path between any two nodes u and v is the total weight of all
    edges in the path connecting them.

    Given a 2D integer array queries. For each queries[i] = [ui, vi], determine
    the number of ways to assign weights to edges in the path such that the cost
    of the path between ui and vi is odd.

    Return an array answer, where answer[i] is the number of valid assignments
    for queries[i].

    Since the answer may be large, apply modulo 10**9 + 7 to each answer[i].
    '''
    # doing the climb up the tree to find common ancestor is O(n) in worst case
    # worst case for all queries is O(n^2)
    def assignEdgeWeights_tle(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        m = 10**9+7
        n = len(edges)+1
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        # node -> [depth, parent, children]
        tree: Dict[List[int]] = defaultdict(list)
        def dfs(node:int,parent:int,depth:int) -> None:
            tree[node] = [depth, parent, list()]
            for i in graph[node]:
                if i != parent:
                    tree[node][2].append(i)
                    dfs(i, node, depth+1)
            return
        def common(a:int, b:int) -> int:
            if a == b:
                return tree[a][0]
            elif tree[a][0] > tree[b][0]:
                return common(tree[a][1], b)
            elif tree[a][0] < tree[b][0]:
                return common(a, tree[b][1])
            else:
                return common(tree[a][1], tree[b][1])
        def query(a:int, b:int) -> int:
            c = common(a,b)
            a = tree[a][0] - c
            b = tree[b][0] - c
            c = a+b
            if c == 0:
                return 0
            return pow(2, c-1, m)
        dfs(1,0,0)
        return [query(i,j) for i,j in queries]

    '''
    Based on Leetcode editorial
    https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/editorial/?envType=daily-question&envId=2026-06-12
    '''
    # data structure for lowest common ancestor
    class LCA:
        def __init__(self, edges:List[List[int]], root:int):
            self.n = len(edges) + 1
            self.m = int(math.log2(self.n)) + 2
            self.edges = [[] for _ in range(self.n + 1)]
            self.depth = [0] * (self.n + 1)
            # ancestor[x][k] -> ancestor reached from node x jumping 2^k nodes up
            self.ancestor = [[0] * self.m for _ in range(self.n + 1)]
            for i,j in edges:
                self.edges[i].append(j)
                self.edges[j].append(i)
            self.dfs(root, 0)
            for i in range(1, self.m):
                for j in range(1, self.n + 1):
                    self.ancestor[j][i] = self.ancestor[self.ancestor[j][i-1]][i-1]
        def dfs(self, node:int, parent:int):
            self.ancestor[node][0] = parent
            for child in self.edges[node]:
                if child == parent:
                    continue
                self.depth[child] = self.depth[node] + 1
                self.dfs(child, node)
        # binary lifting
        def lca(self, x:int, y:int) -> int:
            if self.depth[x] > self.depth[y]:
                x,y = y,x
            # raise node y to depth of node x
            diff = self.depth[y] - self.depth[x]
            for i in range(self.m-1, -1, -1):
                if diff & (1 << i):
                    y = self.ancestor[y][i]
            if x == y:
                return x
            for i in range(self.m-1,-1,-1):
                if self.ancestor[x][i] != self.ancestor[y][i]:
                    x = self.ancestor[x][i]
                    y = self.ancestor[y][i]
            return self.ancestor[x][0]
        def distance(self, x:int, y:int) -> int:
            return self.depth[x] + self.depth[y] - self.depth[self.lca(x,y)] * 2
    def __init__(self):
        self.mod = 10**9 + 7
        self.n = 100010
        self.powersTwo = [0] * self.n
        self.powersTwo[0] = 1
        for i in range(1, self.n):
            self.powersTwo[i] = (self.powersTwo[i-1] * 2) % self.mod
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        lca = Solution.LCA(edges,1)
        answer = []
        for i,j in queries:
            if i == j:
                answer.append(0)
            else:
                answer.append(self.powersTwo[lca.distance(i,j)-1])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2]]
        j = [[1,1],[1,2]]
        o = [0,1]
        self.assertEqual(s.assignEdgeWeights(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[1,3],[3,4],[3,5]]
        j = [[1,4],[3,4],[2,5]]
        o = [2,1,4]
        self.assertEqual(s.assignEdgeWeights(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)