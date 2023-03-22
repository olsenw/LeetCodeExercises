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
    Given a positive integer n representing n cites numbered from 1 to n. Also
    given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that
    there is a bidirectional road between cities ai and bi with a distance equal
    to distancei. The cities graph is not necessarily connected.

    The score of a path between two cities is defined as the minimum distance of
    a road in this path.

    Return the minimum possible score of a path between cities 1 and n.

    Note :
    * A path is a sequence of roads between two cities.
    * It is allowed for a path to contain the same road multiple time, and it is
      possible to visit cities 1 and n multiple times along the path.
    * The test cases are generated such that there is at least one path between
      1 and n.
    '''
    # finds the shortest distance... which is not what question asked
    def minScore_incorrect(self, n: int, roads: List[List[int]]) -> int:
        graph = {i:[] for i in range(1,n+1)}
        for i,j,k in roads:
            graph[i].append((j,k))
            graph[j].append((i,k))
        visited = dict()
        q = [(0,1)]
        while q:
            distance, city = heapq.heappop(q)
            if city == n:
                return distance
            if city in visited and distance >= visited[city]:
                continue
            visited[city] = distance
            for i,j in graph[city]:
                heapq.heappush(q, (distance + j, i))
        return 0

    # Figured out this solution... but thought it was invalid after reading note
    # 2... thought only cities 1 and n could be visited multiple times...
    # Looked at LeetCode solution and figured out what question wanted
    # https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
    # do not like the wording
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {i:[] for i in range(1,n+1)}
        for i,j,k in roads:
            graph[i].append((j,k))
            graph[j].append((i,k))
        answer = 10**5 + 1
        visited = set()
        visited.add(1)
        q = deque([1])
        while q:
            city = q.popleft()
            for i,j in graph[city]:
                answer = min(answer, j)
                if i not in visited:
                    visited.add(i)
                    q.append(i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
        o = 5
        self.assertEqual(s.minScore(i,j), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [[1,2,2],[1,3,4],[3,4,7]]
        o = 2
        self.assertEqual(s.minScore(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = [[1,2,9],[2,3,1],[2,4,5],[1,4,7]]
        o = 1
        self.assertEqual(s.minScore(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)