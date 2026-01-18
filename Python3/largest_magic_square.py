# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A k x k magic square is a k x k grid filled with integers such that every
    row sum, every column sum, and both diagonal sums are all equal. The
    integers in the magic square do not have to be distinct. Every 1 x 1 grid is
    trivially a magic square.

    Given an m x n integer grid, return the size (ie the side length k) of the
    largest magic square that can be found within this grid.
    '''
    def largestMagicSquare_incomplete(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        answer = 1
        rows = [[0] * (n+1) for _ in range(m+1)]
        cols = [[0] * (n+1) for _ in range(m+1)]
        uDig = [[0] * (n+1) for _ in range(m+1)]
        dDig = [[0] * (n+1) for _ in range(m+1)]
        # prefix sum rows
        for i in range(m):
            for j in range(n):
                rows[i+1][j+1] = rows[i+1][j] + grid[i][j]
        # prefix sum columns
        for j in range(n):
            for i in range(m):
                cols[i+1][j+1] = cols[i][j+1] + grid[i][j]
        # prefix sum diagonals top left -> bottom right
        for i in range(m):
            for j in range(n-i):
                dDig[i+1][j+1] = dDig[i][j] + grid[i][j]
        for j in range(1,n):
            for i in range(m-i):
                dDig[i+1][j+1] = dDig[i][j] + grid[i][j]
        # prefix sum diagonals top left -> bottom right
        for i in range(m-1, -1, -1):
            for j in range(n):
                # uDig[i + 1][] = uDig[i+1][] + grid[i][j]
                pass
        return answer

    # indices math wrong
    def largestMagicSquare_fails(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        answer = 1
        for i in range(m):
            for j in range(n):
                for d in range(1,min(m-i,n-j)):
                    rows = [0] * d
                    for x in range(i,i+d):
                        for y in range(j,j+d):
                            rows[x-i] += grid[x][y]
                    if not all(r == rows[0] for r in rows):
                        break
                    cols = [0] * d
                    for y in range(j,j+d):
                        for x in range(i,i+d):
                            cols[y-j] += grid[x][y]
                    if not all(c == rows[0] for c in cols):
                        break
                    diag = 0
                    for x in range(d):
                        diag += grid[i+x][j+x]
                    if diag != rows[0]:
                        break
                    diag = 0
                    for x in range(d):
                        diag += grid[i+d-x][j+x]
                    if diag != rows[0]:
                        break
                    answer = max(answer, d)
        return answer

    # based on leetcode editorial
    # https://leetcode.com/problems/largest-magic-square/editorial/?envType=daily-question&envId=2026-01-18
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        # prefix sum rows
        row = [[0] * n for _ in range(m)]
        for i in range(m):
            row[i][0] = grid[i][0]
            for j in range(1,n):
                row[i][j] += row[i][j-1] + grid[i][j]
        # prefix sum columns
        col = [[0] * n for _ in range(m)]
        for j in range(n):
            col[0][j] = grid[0][j]
            for i in range(1,m):
                col[i][j] = col[i-1][j] + grid[i][j]
        # enumerate on edge length (large -> small)
        for edge in range(min(m,n), 1, -1):
            # select top left of potential magic square
            for i in range(m - edge + 1):
                for j in range(n - edge + 1):
                    # calculate sum of first row
                    s = row[i][j+edge-1]
                    if j != 0:
                        s -= row[i][j-1]
                    flag = True
                    # calculate all rows
                    for x in range(i+1,i+edge):
                        r = row[x][j + edge - 1]
                        if j != 0:
                            r -= row[x][j-1]
                        if r != s:
                            flag = False
                            break
                    if not flag:
                        continue
                    # calculate all columns
                    for y in range(j, j+edge):
                        c = col[i+edge-1][y]
                        if i != 0:
                            c -= col[i-1][y]
                        if c != s:
                            flag = False
                            break
                    if not flag:
                        continue
                    # cal
                    d1 = d2 = 0
                    for z in range(edge):
                        d1 += grid[i+z][j+z]
                        d2 += grid[i+z][j + edge - 1 - z]
                    if d1 == s and d2 == s:
                        return edge
        return 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
        o = 3
        self.assertEqual(s.largestMagicSquare(i), o)

    def test_two(self):
        s = Solution()
        i = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
        o = 2
        self.assertEqual(s.largestMagicSquare(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)