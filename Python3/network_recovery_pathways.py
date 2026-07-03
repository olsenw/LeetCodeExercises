# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a directed acyclic graph of n nodes numbered from 0 to n - 1. This is
    represented by a 2D array edges of length m, where edges[i] = [ui,vi,costi]
    indicates a one-way communication from node ui to node vi with a recovery
    cost of costi.

    Some nodes may be offline. Given a boolean array online where
    online[i] = true means node i is online. Nodes 0 and n - 1 are always
    online.

    A path from 0 to n - 1 is valid if:
    * All intermediate nodes on the path are online.
    * The total recovery cost of all edges on the path does not exceed k.

    For each valid path, define its score as the minimum edge-cost along that
    path.

    Return the maximum path score (ie, the largest minimum edge cost) among all
    valid paths. If no valid path exists, return -1.
    '''
    # finds the correct answer, but exploring every path is slow
    def findMaxPathScore_tle(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = [set() for _ in range(n)]
        for i,j,c in edges:
            if online[j]:
                graph[i].add((j,c))
        def dfs(node:int, cost:int, minimum:int) -> int:
            if node == n-1:
                return minimum if cost <= k else -1
            answer = -1
            for i,c in graph[node]:
                answer = max(answer, dfs(i, cost + c, min(minimum, c)))
            return answer
        return dfs(0, 0, 10**9+7)

    # based on hints
    # binary search on largest minimum edge
    # Dijkstra to validate
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        left = right = 0
        graph = [set() for _ in range(n)]
        for i,j,c in edges:
            if online[j]:
                graph[i].add((j,c))
                right = max(right, c)
        # based on Wikipedia's Dijkstra priority queue pseudocode
        def test(edgeBound:int) -> bool:
            distance = [float('inf')] * n
            # cost of path, node
            queue = [(0,0)]
            while queue:
                c,i = heapq.heappop(queue)
                if distance[i] <= c:
                    continue
                distance[i] = c
                if i == n-1 and distance[n-1] <= k:
                    return True
                for j,e in graph[i]:
                    if e >= edgeBound:
                        heapq.heappush(queue, (c+e, j))
            return False
        answer = -1
        while left <= right:
            mid = left + (right - left) // 2
            if test(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]]
        j = [True,True,True,True]
        k = 10
        o = 3
        self.assertEqual(s.findMaxPathScore(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]]
        j =[True,True,True,False,True]
        k = 12
        o = 6
        self.assertEqual(s.findMaxPathScore(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [[0,1,8]]
        j = [True,True]
        k = 11
        o = 8
        self.assertEqual(s.findMaxPathScore(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)