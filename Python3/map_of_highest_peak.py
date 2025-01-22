# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer matrix isWater of size m x n that represents a map of land
    and water cells.
    * If isWater[i][j] == 0, cell (i,j) is a land cell.
    * If isWater[i][j] == 1, cell (i,j) is a water cell.

    Assign each cell a height following these rules:
    * The height of each cell must be non-negative.
    * If the cell is a water cell, its height must be 0.
    * Any two adjacent cells must have an absolute height difference of at most
      1. A cell is adjacent to another cell if the former is directly north,
      east, south, or west of the latter (ie, their sides are touching).
    
    Find an assignment of heights such that the maximum height in the matrix is
    maximized.

    Return an integer matrix height of size m x n where height[i][j] is cell
    (i,j)'s height. If there are multiple solutions; return any of them.
    '''
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m,n = len(isWater), len(isWater[0])
        answer = [[-1] * n for _ in range(m)]
        heap = [(0,i,j) for i in range(m) for j in range(n) if isWater[i][j] == 1]
        heapq.heapify(heap)
        while heap:
            h,i,j = heapq.heappop(heap)
            if isWater[i][j] == 1:
                answer[i][j] = 0
            if i > 0 and answer[i-1][j] == -1:
                answer[i-1][j] = h + 1
                heapq.heappush(heap, (h+1,i-1,j))
            if i < m - 1 and answer[i+1][j] == -1:
                answer[i+1][j] = h + 1
                heapq.heappush(heap, (h+1,i+1,j))
            if j > 0 and answer[i][j-1] == -1:
                answer[i][j-1] = h + 1
                heapq.heappush(heap, (h+1,i,j-1))
            if j < n - 1 and answer[i][j+1] == -1:
                answer[i][j+1] = h + 1
                heapq.heappush(heap, (h+1,i,j+1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[0,0]]
        o = [[1,0],[2,1]]
        self.assertEqual(s.highestPeak(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0,1],[1,0,0],[0,0,0]]
        o = [[1,1,0],[0,1,1],[1,2,2]]
        self.assertEqual(s.highestPeak(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)