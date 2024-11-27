# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n and a 2D integer array queries.

    There are n cities numbered from 0 to n - 1. Initially, there is a
    unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

    queries[i] = [ui, vi] represents the addition of a new unidirectional road
    from city ui to city vi. After each query, find the length of the shortest
    path from city 0 to city n - 1.

    Return an array answer where for each i in the range
    [0, queries.length - 1], answer[i] is the length of the shortest path from
    city 0 to city n - 1 after processing the first i + 1 queries.
    '''
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = {i:[i+1] for i in range(n-1)}
        graph[n-1] = []
        def bfs():
            q = deque([(0,0)])
            v = set()
            while q:
                c,d = q.popleft()
                if c in v:
                    continue
                v.add(c)
                if c == n - 1:
                    return d
                for i in graph[c]:
                    if i not in v:
                        q.append((i,d+1))
            return 0
        answer = []
        for a,b in queries:
            graph[a].append(b)
            answer.append(bfs())
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [[2,4],[0,2],[0,4]]
        o = [3,2,1]
        self.assertEqual(s.shortestDistanceAfterQueries(i,j), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [[0,3],[0,2]]
        o = [1,1]
        self.assertEqual(s.shortestDistanceAfterQueries(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)