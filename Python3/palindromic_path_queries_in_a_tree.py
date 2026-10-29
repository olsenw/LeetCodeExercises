# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    # test case 982/1040
    def palindromePath_memory_limit(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        answer = []
        s = list(s)
        graph = {i:[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        @cache
        def dfs(parent:int, node:int, target:int) -> List[int]:
            if node == target:
                return [target]
            for i in graph[node]:
                if i == parent:
                    continue
                path = dfs(node, i, target)
                if path:
                    return path + [node]
            return []
        dfs.cache_clear()
        def isPalindrome(nodes:List[int]):
            c = Counter()
            for i in nodes:
                c[s[i]] += 1
            return sum(c[i] % 2 for i in c) < 2
        for q in queries:
            q = q.split()
            if q[0] == "update":
                s[int(q[1])] = q[2]
            else:
                answer.append(isPalindrome(dfs(n, int(q[1]), int(q[2]))))
        return answer

    # based on Leetcode editorial
    # https://leetcode.com/problems/palindromic-path-queries-in-a-tree/editorial/?envType=daily-question&envId=2026-10-29
    # cool data structure
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # Binary Index Tree
        class BIT:
            def __init__(self, n:int):
                self.n = n
                self.tree = [0] * (n+1)

            @staticmethod
            def lowbit(x:int) -> int:
                return x & -x

            def update(self, x:int, v:int) -> None:
                while x <= self.n:
                    self.tree[x] ^= v
                    x += BIT.lowbit(x)

            def query(self, x:int) -> int:
                answer = 0
                while x:
                    answer ^= self.tree[x]
                    x -= BIT.lowbit(x)
                return answer

            def updateRange(self, l:int, r:int, v:int) -> None:
                self.update(l,v)
                self.update(r+1,v)

        graph = [[] for _ in range(n)]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        LOG = n.bit_length()
        fa = [[0] * LOG for _ in range(n)]
        dep = [0] * n
        l = [0] * n
        r = [0] * n
        timer = 0

        def dfs(i:int, parent:int) -> None:
            nonlocal timer
            timer += 1
            l[i] = timer
            fa[i][0] = parent
            for j in graph[i]:
                if j == parent:
                    continue
                dep[j] = dep[i] + 1
                dfs(j,i)
            r[i] = timer

        dfs(0,0)

        for j in range(1, LOG):
            for i in range(n):
                fa[i][j] = fa[fa[i][j-1]][j-1]

        # least common ancestor
        def lca(i:int, j:int) -> int:
            if dep[i] < dep[j]:
                i,j = j,i
            diff = dep[i] - dep[j]
            for a in range(LOG):
                if (diff >> a) & 1:
                    i = fa[i][a]
            if i == j:
                return i
            for a in range(LOG-1, -1, -1):
                if fa[i][a] != fa[j][a]:
                    i = fa[i][a]
                    j = fa[j][a]
            return fa[i][0]

        bit = BIT(n+1)
        s = list(s)
        for i in range(n):
            bit.updateRange(l[i], r[i], 1 << (ord(s[i]) - ord("a")))

        answer = []
        for q in queries:
            operation, *parms = q.split()
            if operation == "update":
                i, c = int(parms[0]), parms[1]
                bit.updateRange(l[i], r[i], (1 << (ord(s[i]) - ord("a"))) ^ (1 << (ord(c) - ord("a"))))
                s[i] = c
            else:
                i,j = int(parms[0]), int(parms[1])
                w = lca(i,j)
                mask = bit.query(l[i]) ^ bit.query(l[j]) ^ (1 << (ord(s[w]) - ord("a")))
                answer.append(mask.bit_count() <= 1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[0,1],[1,2]]
        k = "aac"
        l = ["query 0 2","update 1 b","query 0 2"]
        o = [True,False]
        self.assertEqual(s.palindromePath(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [[0,1],[0,2],[0,3]]
        k = "abca"
        l = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]
        o = [False,False,True]
        self.assertEqual(s.palindromePath(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)