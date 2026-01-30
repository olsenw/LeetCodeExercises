# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 0-indexed strings sources and target, both of length n and
    consisting of lowercase English characters. Also given two 0-indexed string
    arrays original and changed, and an integer array cost, where cost[i]
    represents the cost of converting the string original[i] to the string
    changed[i].

    Starting with the string source. In one operation pick a substring x from
    the string, and a change it to y at a cost of z if there exists any index j
    such that cost[j] == z, original[j] == x, and changed[j] == y. It is
    possible to do any number of operations, but any pair of operations must
    satisfy either of these two conditions:
    * The substrings picked in the operations are source[a..b] and source[c..d]
      with either b < c or d < a. In other words, the indices picked in both
      operations are disjoint.
    * The substrings picked in the operations are source[a..b] and source[c..d]
      with a == c and b == d. In other words, the indices picked in both
      operations are identical.
    
    Return the minimum cost to convert the string source to the string target
    using any number of operations. If it is impossible to convert source to
    target, return -1.

    Note that there may exist indices i,j such that original[j] == original[i]
    and changed[j] == changed[i].
    ''' 
    # based on Leetcode
    # https://leetcode.com/problems/minimum-cost-to-convert-string-ii/editorial/?envType=daily-question&envId=2026-01-30
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        m = len(original)

        child = [[-1] * 26]
        tid = [-1]

        def new_node() -> int:
            child.append([-1] * 26)
            tid.append(-1)
            return len(child) - 1
        
        index = -1

        def add(word:str) -> int:
            nonlocal index
            node = 0
            for ch in word:
                c = ord(ch) - 97
                nxt = child[node][c]
                if nxt == -1:
                    nxt = new_node()
                    child[node][c] = nxt
                node = nxt
            if tid[node] == -1:
                index += 1
                tid[node] = index
            return tid[node]
        
        edges = []
        for i in range(m):
            x = add(original[i])
            y = add(changed[i])
            edges.append((x,y,cost[i]))
        
        # corner case, if there are no ways to convert, exit early
        p = index + 1
        if p == 0:
            return 0 if source == target else -1
        
        dist = [[float('inf')] * p for _ in range(p)]
        for i in range(p):
            dist[i][i] = 0
        for x,y,w in edges:
            if w < dist[x][y]:
                dist[x][y] = w
        
        for k in range(p):
            dk = dist[k]
            for i in range(p):
                di = dist[i]
                dik = di[k]
                if dik == float('inf'):
                    continue
                base = dik
                for j in range(p):
                    nd = base + dk[j]
                    if nd < di[j]:
                        di[j] = nd
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        sarr = [ord(c) - 97 for c in source]
        tarr = [ord(c) - 97 for c in target]

        for j in range(n):
            if dp[j] >= float('inf'):
                continue

            base = dp[j]

            if source[j] == target[j] and base < dp[j + 1]:
                dp[j + 1] = base
            
            u = 0
            v = 0
            for i in range(j,n):
                u = child[u][sarr[i]]
                v = child[v][tarr[i]]
                if u == -1 or v == -1:
                    break
                uid = tid[u]
                vid = tid[v]
                if uid != -1 and vid != -1:
                    w = dist[uid][vid]
                    if w != float('inf'):
                        ni = i + 1
                        cand = base + w
                        if cand < dp[ni]:
                            dp[ni] = cand
        answer = dp[n]
        return -1 if answer >= float('inf') else answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcd"
        j = "acbe"
        k = ["a","b","c","c","e","d"]
        l = ["b","c","b","e","b","e"]
        m = [2,5,5,1,2,20]
        o = 28
        self.assertEqual(s.minimumCost(i,j,k,l,m), o)

    def test_two(self):
        s = Solution()
        i = "abcdefgh"
        j = "acdeeghh"
        k = ["bcd","fgh","thh"]
        l = ["cde","thh","ghh"]
        m = [1,3,5]
        o = 9
        self.assertEqual(s.minimumCost(i,j,k,l,m), o)

    def test_three(self):
        s = Solution()
        i = "abcdefgh"
        j = "addddddd"
        k = ["bcd","defgh"]
        l = ["ddd","ddddd"]
        m = [100,1578]
        o = -1
        self.assertEqual(s.minimumCost(i,j,k,l,m), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)