# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A city is represented as a bi-directional connected graph with n vertices
    where each vertex is labeled from 1 to n (inclusive). The edges in the graph
    are represented as a 2D integer array edges, where each edges[i] = [ui, vi]
    denotes a bi-directional edge between vertex ui and vertex vi. Every vertex
    pair is connected by at most one edge, and no vertex has an edge to itself.
    The time taken to traverse any edge is time minutes.

    Each vertex has a traffic signal which changes its color from green to red
    and vice versa every change minutes. All signals change at the same time. It
    is possible to enter a vertex at any time, but it is only possible to leave
    a vertex when the signal is green. It is not possible to wait at a vertex if
    the signal is green.

    The second minimum value is defined as the smallest value strictly larger
    than the minimum value.

    Given n, edges, time, and change, return the second minimum time it will
    take to go from vertex 1 to vertex n.

    Notes:
    * It is possible to traverse any vertex any number of times, including 1 and
      n.
    * It is assumed that all signals are green when the journey starts.
    '''
    def secondMinimum_wrong(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n+1)]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        a = False
        h = [(0,1)]
        v = defaultdict(list)
        while h:
            y,x = heapq.heappop(h)
            if x in v and len(v[x]) > 1 and v[x][-1] < y:
                continue
            while len(v[x]>2) and y < v[x][-1]:
                v[x].pop()
            v[x].append(y)
            # if x == n:
            #     if a:
            #         return y
            #     else:
            #         a = True
            color, remain = divmod(y, change)
            if color % 2:
                for z in graph[x]:
                    heapq.heappush(h, (y + time + (change - remain), z))
            else:
                for z in graph[x]:
                    heapq.heappush(h, (y + time, z))
        return v[n][-1]

    def secondMinimum_slow(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n+1)]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        h = [(0,1)]
        # shortest time to visit node
        v1 = [float('inf')] * (n+1)
        # 2nd shortest time to visit node
        v2 = [float('inf')] * (n+1)
        while h:
            y,x = heapq.heappop(h)
            if y < v1[x]:
                v2[x], v1[x] = v1[x], y
            # this change is important
            # elif y < v2[x]:
            elif v1[x] < y < v2[x]:
                v2[x] = y
            else:
                continue
            color, remain = divmod(y, change)
            if color % 2:
                for z in graph[x]:
                    t = y + time + (change - remain)
                    if t < v2[z]:
                        heapq.heappush(h, (t, z))
            else:
                for z in graph[x]:
                    t = y + time
                    if t < v2[z]:
                        heapq.heappush(h, (t, z))
        return v2[n]

    # based on help from Leetcode editorial
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n+1)]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        # shortest time to node
        dist1 = [float('inf')] * (n+1)
        # 2nd shortest time to node
        dist2 = [float('inf')] * (n+1)
        # how often node is popped off the queue
        freq = [0] * (n+1)
        # priority queue of time and node
        h = [(0,1)]
        # modified Dijkstra
        while h:
            y,x = heapq.heappop(h)
            freq[x] += 1
            # target node for 2nd time
            if x == n and freq[x] == 2:
                return dist2[n]
            color, remain = divmod(y, change)
            # t = y + time
            # if color % 2:
            #     t += (change - remain)
            if color % 2:
                t = change * (color + 1) + time
            else:
                t = y + time
            for z in graph[x]:
                if freq[z] == 2:
                    continue
                if t < dist1[z]:
                    dist2[z], dist1[z] = dist1[z], t
                    heapq.heappush(h, (t,z))
                elif dist1[z] < t < dist2[z]:
                    dist2[z] = t
                    heapq.heappush(h, (t,z))
        # default case of graph having single node
        return 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [[1,2],[1,3],[1,4],[3,4],[4,5]]
        k = 3
        l = 5
        o = 13
        self.assertEqual(s.secondMinimum(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [[1,2]]
        k = 3
        l = 2
        o = 11
        self.assertEqual(s.secondMinimum(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)