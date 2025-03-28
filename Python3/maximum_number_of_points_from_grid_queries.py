# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n integer matrix grid and an array queries of size k.

    Find an array answer of size k such that for each integer queries[i] start
    at the top left cell of the matrix and repeat the following process:
    * If queries[i] is strictly greater than the value of the current cell
      currently occupied, then gain one point if this is the first time visiting
      this cell, and then move to any adjacent cell in all 4 directions: up,
      down, left, and right.
    * Otherwise, obtain no points and end the process.

    After the process, answer[i] is the maximum number of points that can be
    obtained. Note that for each query it is possible to visit the same cell
    multiple times.

    Return the resulting array answer.
    '''
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m,n = len(grid), len(grid[0])
        answer = []
        order = sorted(range(len(queries)), key=lambda x:queries[x])
        heap = [(grid[0][0], 0, 0)]
        score = 0
        visited = {(0,0)}
        for i in order:
            q = queries[i]
            pass
            while heap and heap[0][0] < q:
                _,x,y = heapq.heappop(heap)
                score += 1
                if x > 0 and (x-1,y) not in visited:
                    visited.add((x-1,y))
                    heapq.heappush(heap, (grid[x-1][y],x-1,y))
                if x < m - 1 and (x+1,y) not in visited:
                    visited.add((x+1,y))
                    heapq.heappush(heap, (grid[x+1][y],x+1,y))
                if y > 0 and (x,y-1) not in visited:
                    visited.add((x,y-1))
                    heapq.heappush(heap, (grid[x][y-1],x,y-1))
                if y < n - 1 and (x,y+1) not in visited:
                    visited.add((x,y+1))
                    heapq.heappush(heap, (grid[x][y+1],x,y+1))
            answer.append((i,score))
        return [a for _,a in sorted(answer)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[2,5,7],[3,5,1]]
        j = [5,6,2]
        o = [5,8,1]
        self.assertEqual(s.maxPoints(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[5,2,1],[1,1,2]]
        j = [3]
        o = [0]
        self.assertEqual(s.maxPoints(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)