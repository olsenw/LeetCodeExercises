# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents
    the number of points at position (r,c) on the matrix. Two robots are playing
    a game on this matrix.

    Both robots initially start at (0,0) and want to reach (1,n-1). Each robot
    may only move to the right ((r,c) to (r,c+1)) or down ((r,c) to (r+1,c)).

    At the start of the game, the first robot moves from (0,0) to (1,n-1),
    collecting all the points from the cells on its path. For all cells (r,c)
    traversed on the path, grid[r][c] is set to 0. Then, the second robot moves
    from (0,0) to (1,n-1), collecting the points on its path. Note that their
    paths may intersect with one another.

    The first robot wants to minimize the number of points collected by the
    second robot. In contrast, the second robot wants to maximize the number of
    points it collects. If both robots play optimally, return the number of
    points collected by the second robot.
    '''
    # assumes the best play is for robot 1 to maximize score
    # this is not the case
    def gridGame_fails(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top = [0]
        bottom = [0]
        for i in range(n):
            top.append(top[-1] + grid[0][i])
            bottom.append(bottom[-1] + grid[1][n-1-i])
        top = top[1:]
        bottom = bottom[1:][::-1]
        robot1 = 0,0
        for i in range(n):
            a = top[i] + bottom[i]
            if a > robot1[0]:
                robot1 = a,i
        top = [0]
        bottom = [0]
        for i in range(n):
            if i <= robot1[1]:
                top.append(0)
            else:
                top.append(top[-1] + grid[0][i])
            if n-1-i >= robot1[1]:
                bottom.append(0)
            else:
                bottom.append(bottom[-1] + grid[1][n-1-i])
        top = top[1:]
        bottom = bottom[1:][::-1]
        robot2 = 0,0
        for i in range(n):
            a = top[i] + bottom[i]
            if a > robot2[0]:
                robot2 = a,i
        return robot2[0]

    # O(n^2)
    def gridGame_tle(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top = [0]
        bottom = [0]
        for i in range(n):
            top.append(top[-1] + grid[0][i])
            bottom.append(bottom[-1] + grid[1][n-1-i])
        top = top[1:]
        bottom = bottom[1:][::-1]
        answer = float('inf')
        for i in range(n):
            a = 0
            for j in range(n):
                t = 0 if j <= i else top[j] - top[i]
                b = 0 if i <= j else bottom[j] - bottom[i]
                a = max(a, t+b)
            answer = min(answer, a)
        return answer

    # note optimal play for robot2 is to take all of top or all of bottom
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top = [0]
        bottom = [0]
        for i in range(n):
            top.append(top[-1] + grid[0][i])
            bottom.append(bottom[-1] + grid[1][n-1-i])
        top = top[1:]
        bottom = bottom[1:][::-1]
        answer = float('inf')
        for i in range(n):
            t = top[-1] - top[i]
            b = bottom[0] - bottom[i]
            answer = min(answer, max(t,b))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,5,4],[1,5,1]]
        o = 4
        self.assertEqual(s.gridGame(i), o)

    def test_two(self):
        s = Solution()
        i = [[3,3,1],[8,5,2]]
        o = 4
        self.assertEqual(s.gridGame(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,3,1,15],[1,3,3,1]]
        o = 7
        self.assertEqual(s.gridGame(i), o)

    def test_four(self):
        s = Solution()
        i = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]
        o = 63
        self.assertEqual(s.gridGame(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)