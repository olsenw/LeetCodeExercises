# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
from functools import cache
import heapq
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are n cities connected by some number of flights. Given an array
    flights where flights[i] = [fromi, toi, pricei] indicates that there is a
    flight from city fromi to city cityi with cost pricei.

    Also given three integers src, dst, and k, return the cheapest price from
    src to dst with at most k stops. If there is no such route, return -1.
    '''
    # bfs tle many possible retreads
    def findCheapestPrice_bfs_tle(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i:[] for i in range(n)}
        for a,b,c in flights:
            graph[a].append((b,c))
        answer = math.inf
        visited = dict()
        queue = deque([(0, src, k)])
        while queue:
            price, city, jumps = queue.popleft()
            if city == dst:
                answer = min(answer, price)
                continue
            visited[city] = price
            for c,p in graph[city]:
                if (c not in visited or visited[c] > price + p) and jumps >= 0:
                    queue.append((price + p, c, jumps - 1))
        return -1 if answer == math.inf else answer

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i:[] for i in range(n)}
        for a,b,c in flights:
            graph[a].append((b,c))
        @cache
        def dfs(city, jumps):
            if jumps > k + 1:
                return -1
            if city == dst:
                return 0
            answer = math.inf
            for c,p in graph[city]:
                a = dfs(c,jumps + 1)
                if a > -1:
                    answer = min(answer, a + p)
            return -1 if answer == math.inf else answer
        return dfs(src, 0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
        k = 0
        l = 3
        m = 1
        o = 700
        self.assertEqual(s.findCheapestPrice(i,j,k,l,m), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[0,1,100],[1,2,100],[0,2,500]]
        k = 0
        l = 2
        m = 1
        o = 200
        self.assertEqual(s.findCheapestPrice(i,j,k,l,m), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [[0,1,100],[1,2,100],[0,2,500]]
        k = 0
        l = 2
        m = 0
        o = 500
        self.assertEqual(s.findCheapestPrice(i,j,k,l,m), o)

    def test_four(self):
        s = Solution()
        i = 5
        j = [[0,1,100],[0,2,100],[0,3,10],[1,2,100],[1,4,10],[2,1,10],[2,3,100],[2,4,100],[3,2,10],[3,4,100]]
        k = 0
        l = 4
        m = 3
        o = 40
        self.assertEqual(s.findCheapestPrice(i,j,k,l,m), o)

    def test_five(self):
        s = Solution()
        i = 5
        j = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
        k = 0
        l = 2
        m = 2
        o = 7
        self.assertEqual(s.findCheapestPrice(i,j,k,l,m), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)