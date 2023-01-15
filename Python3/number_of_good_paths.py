# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict, deque
from math import comb
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a tree consisting of n nodes numbered from 0 to n - 1 and exactly
    n - 1 edges.

    Given a 0-indexed integer array vals of length n where vals[i] denotes the
    value of the ith node. Also given a 2D integer array edges where
    edges[i] = [ai, bi] denotes that there exists an undirected edge connecting
    nodes ai and bi.

    A good path is a simple path that satisfies the following conditions:

    The starting node and the ending node have the same value.

    All nodes between the starting node and the ending node have values less
    than or equal to the starting node (ie the starting nodes value should e the
    maximum value along the path).

    Return the number of distinct good paths.

    Note that a path and its reverse are counted as the same path. For example
    0 -> i is considered to be the same as i -> 0. A single node is also
    considered as a valid path.
    '''
    # TLE 123/134 cases
    def numberOfGoodPaths_bfs_tle(self, vals: List[int], edges: List[List[int]]) -> int:
        # tree as an undirected graph
        g = {i:[] for i in range(len(vals))}
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        # set of nodes marked/found (prevent double count paths)
        marked = set()
        # bfs that terminates on nodes larger than start (returns valid paths)
        def bfs(n:int) -> int:
            if n in marked:
                return 0
            # marked.add(n)
            p = 0
            v = set()
            q = deque([n])
            while q:
                a = q.popleft()
                if a in v:
                    continue
                v.add(a)
                if vals[a] == vals[n]:
                    p += 1
                    marked.add(a)
                for b in g[a]:
                    if vals[b] <= vals[n]:
                        q.append(b)
                    pass
            # return p - 1
            return comb(p,2)
        # return number of nodes (singles count) plus valid paths for each node
        return len(vals) + sum(bfs(i) for i in range(len(vals)))

    # TLE 123/134 cases
    def numberOfGoodPaths_dfs_tle(self, vals: List[int], edges: List[List[int]]) -> int:
        # tree as an undirected graph
        g = {i:[] for i in range(len(vals))}
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        # set of nodes marked/found (prevent double count paths)
        marked = set()
        # dfs that terminates on nodes larger than start (returns valid paths)
        visited = set()
        def dfs(n:int, target:int) -> int:
            visited.add(n)
            p = 0
            if vals[n] == target:
                p += 1
                marked.add(n)
            for e in g[n]:
                if e not in visited and vals[e] <= target:
                    p += dfs(e, target)
            visited.remove(n)
            return p
        # return number of nodes (singles count) plus valid paths for each node
        return len(vals) + sum(comb(dfs(i, vals[i]),2) for i in range(len(vals)) if i not in marked)

    # Leetcode solution posted by augustus3
    # https://leetcode.com/problems/number-of-good-paths/solutions/3053167/python-union-find-with-detailed-explanation-time-complexity-o-n-logn/?orderBy=most_votes&languageTags=python3&topicTags=union-find
    # makes use of union find
    # build graph(s) using smallest then adding next size bigger nodes (previous
    # graphs are single node in new one because acyclic tree), repeat
    # Leetcode card on disjoint sets (union find in many parts)
    # https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3881/
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        ans = 0
        n = len(vals)
        f = list(range(n))
        dct = defaultdict(list)
        mp = [[] for _ in range(n)]

        def find(u):
            if f[u] == u:
                return u

            f[u] = find(f[u])
            return f[u]

        def merge(u, v):
            fu, fv = find(u), find(v)
            if fu != fv:
                f[fu] = fv

        for i, val in enumerate(vals):
            dct[val].append(i)

        for u, v in edges:
            uVal, vVal = vals[u], vals[v]
            if uVal >= vVal:
                mp[u].append(v)
            else:
                mp[v].append(u)

        keys = sorted(dct.keys())
        for key in keys:
            arr = dct[key]
            for u in arr:
                for v in mp[u]:
                    merge(u, v)

            groups = defaultdict(list)
            for u in arr:
                groups[find(u)].append(u)

            for root, nodes in groups.items():
                ln = len(nodes)
                ans += ln*(ln+1)>>1

        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2,1,3]
        j = [[0,1],[0,2],[2,3],[2,4]]
        o = 6
        self.assertEqual(s.numberOfGoodPaths(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2,2,3]
        j = [[0,1],[1,2],[2,3],[2,4]]
        o = 7
        self.assertEqual(s.numberOfGoodPaths(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1]
        j = []
        o = 1
        self.assertEqual(s.numberOfGoodPaths(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,1,1]
        j = [[0,1],[0,2]]
        o = 6
        self.assertEqual(s.numberOfGoodPaths(i,j), o)

    def test_five(self):
        s = Solution()
        i = [1,1,1,1,1]
        j = [[0,1],[0,2],[2,3],[2,4]]
        o = 15
        self.assertEqual(s.numberOfGoodPaths(i,j), o)

    def test_six(self):
        s = Solution()
        i = [1,1,2,1,1,1,2]
        j = [[0,1],[0,2],[2,3],[2,4],[4,5],[4,6]]
        o = 10
        self.assertEqual(s.numberOfGoodPaths(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)