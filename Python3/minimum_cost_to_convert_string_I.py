# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict, deque
from functools import cache
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 0-indexed strings source and target, both of length n and
    consisting of lowercase English letters. Also given two 0-indexed character
    array original and changed, and an integer array cost, where cost[i]
    represents the cost of changing the character original[i] to the character
    changed[i].

    Start with the string source. In one operation, pick a character x from the
    string and change it to the character y at a cost of z if there exists any
    index j such that cost[j] == z, original[j] == x and changed[j] == y.

    Return the minimum cost to convert the string source to the string target
    using any number of operations. If it is impossible to convert source to
    target, return -1.

    Note that there may exist indices i,j such that original[j] == original[i]
    and changed[j] == changed[i]
    '''
    def minimumCost_wrong(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(dict)
        for i in range(len(cost)):
            if changed[i] in graph[original[i]]:
                graph[original[i]][changed[i]] = min(cost[i], graph[original[i]][changed[i]])
            else:
                graph[original[i]][changed[i]] = cost[i]
        @cache
        def bfs(i,j):
            q = deque([(i,0)])
            v = set()
            while q:
                x,y = q.popleft()
                if x == j:
                    return y
                if x in v:
                    continue
                v.add(x)
                for z in graph[x]:
                    q.append((z,y + graph[x][z]))
            return -1
        answer = 0
        for x,y in zip(source, target):
            a = bfs(x,y)
            if a == -1:
                return -1
            answer += a
        return answer

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(dict)
        for i in range(len(cost)):
            if changed[i] in graph[original[i]]:
                graph[original[i]][changed[i]] = min(cost[i], graph[original[i]][changed[i]])
            else:
                graph[original[i]][changed[i]] = cost[i]
        @cache
        def bfs(i,j):
            h = [(0,i)]
            v = set()
            while h:
                y,x = heapq.heappop(h)
                if x == j:
                    return y
                v.add(x)
                for z in graph[x]:
                    if z not in v:
                        heapq.heappush(h, (y + graph[x][z], z))
            return -1
        answer = 0
        for x,y in zip(source, target):
            a = bfs(x,y)
            if a == -1:
                return -1
            answer += a
        return answer

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
        i = "aaaa"
        j = "bbbb"
        k = ["a","c"]
        l = ["c","b"]
        m = [1,2]
        o = 12
        self.assertEqual(s.minimumCost(i,j,k,l,m), o)

    def test_three(self):
        s = Solution()
        i = "abcd"
        j = "abce"
        k = ["a"]
        l = ["e"]
        m = [10000]
        o = -1
        self.assertEqual(s.minimumCost(i,j,k,l,m), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)