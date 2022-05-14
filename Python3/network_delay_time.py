# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import deque
import heapq
class Solution:
    '''
    Given a network of n nodes labeled from 1 to n. Given times, a list
    of travel times as directed edges time[i] = (ui,vi,wi), where ui is
    the source node, vi is the target node, and wi is the time it takes
    for a signal to travel from source to target.

    A signal is sent from a given node k. Return the time it takes for
    all the n nodes to receive the signal. If it is impossible for all
    the nodes to receive the signal return -1.
    '''
    def networkDelayTime_bfs(self, times: List[List[int]], n: int, k: int) -> int:
        g = {i:[] for i in range(n)}
        for x,y,z in times:
            g[x - 1].append((y - 1, z))
        d = [float('inf')] * n
        d[k - 1] = 0
        q = deque([k - 1])
        while q:
            c = q.popleft()
            for i,j in g[c]:
                if d[c] + j < d[i]:
                    d[i] = d[c] + j
                    q.append(i)
        m = max(d)
        return m if m < float('inf') else -1

    # Dijkstra
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = {i:[] for i in range(n)}
        for x,y,z in times:
            g[x - 1].append((y - 1, z))
        d = [float('inf')] * n
        d[k - 1] = 0
        h = [(0, k - 1)]
        while h:
            w, c = heapq.heappop(h)
            if w > d[c]:
                continue
            for i,j in g[c]:
                if w + j < d[i]:
                    d[i] = w + j
                    heapq.heappush(h, (d[i], i))
        m = max(d)
        return m if m < float('inf') else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,1,1],[2,3,1],[3,4,1]]
        j = 4
        k = 2
        o = 2
        self.assertEqual(s.networkDelayTime(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,1]]
        j = 2
        k = 1
        o = 1
        self.assertEqual(s.networkDelayTime(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [[1,2,1]]
        j = 2
        k = 2
        o = -1
        self.assertEqual(s.networkDelayTime(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
        j = 3
        k = 2
        o = 6
        self.assertEqual(s.networkDelayTime(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)