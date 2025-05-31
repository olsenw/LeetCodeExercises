# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an n x n integer matrix board where the cells are labeled from 1 to
    n^2 in a Boustrophedon style starting from the bottom left of the board (ie
    board[n-1][0]) and alternating direction each row.

    Place a character on square 1 of the board. In each move, starting from
    square curr, do the following:
    * Choose a destination square next with a label in the range
      [curr + 1, min(curr + 6, n^2)].
      * This choice simulates the result of a standard 6-sided die roll.
    * If next has a snake or ladder, the character must move to the destination
      of that snake or ladder. Otherwise the character moves to next.
    * The game ends when the character reaches square n^2.

    A board square on row r and column c has a snake or ladder if
    board[r][c] != -1. The destination of that snake or ladder is board[r][c].
    Squares 1 and n^2 do not have a snake or ladder.

    Note that it is only possible to traverse a single snake or ladder per move.
    If the destination to a snake or ladder is the start of another snake or
    ladder the character does not make a subsequent move.

    Return the least number of moves required to reach the square n^2. If it is
    not possible to reach the square return -1.
    '''
    # use of min heap in bfs was unneeded
    def snakesAndLadders_tle(self, board: List[List[int]]) -> int:
        # turn 2d array into 1d array (note it is one indexed)
        flattened = []
        reverse = False
        for r in board[::-1]:
            if reverse:
                flattened.extend(r[::-1])
            else:
                flattened.extend(r)
            reverse = not reverse
        # keep track of number of jumps to visit square
        jumps = [-1] * len(flattened)
        # preform bfs
        heap = [(0,1)]
        while heap:
            m, n = heapq.heappop(heap)
            if n == len(flattened):
                return m
            jumps[n - 1] = m
            for j in range(n + 1, min(n + 6, len(flattened)) + 1):
                land = flattened[j - 1] if flattened[j - 1] > 0 else j
                if jumps[land - 1] == -1 or m + 1 < jumps[land - 1]:
                    heapq.heappush(heap, (m + 1, land))
        return -1

    # works, but is slow and memory intensive
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # turn 2d array into 1d array (note it is one indexed)
        flattened = []
        reverse = False
        for r in board[::-1]:
            if reverse:
                flattened.extend(r[::-1])
            else:
                flattened.extend(r)
            reverse = not reverse
        # keep track of number of jumps to visit square
        jumps = [-1] * len(flattened)
        # preform bfs
        queue = deque([(0,1)])
        while queue:
            m, n = queue.popleft()
            if n == len(flattened):
                return m
            jumps[n - 1] = m
            for j in range(n + 1, min(n + 6, len(flattened)) + 1):
                land = flattened[j - 1] if flattened[j - 1] > 0 else j
                if jumps[land - 1] == -1 or m + 1 < jumps[land - 1]:
                    queue.append((m + 1, land))
        return -1

    '''
    other solutions also do bfs, but have smarter index systems (ie dont flatten)
    '''
    # 5.30.25 old solution no longer passes
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        flatten = []
        reverse = False
        index = 0
        for row in board[::-1]:
            if reverse:
                row = row[::-1]
            for c in row:
                flatten.append(index if c == -1 else c - 1)
                index += 1
            reverse = not reverse
        jumps = [10**5] * (n * n)
        queue = [(0,0)]
        while queue:
            hops, i = heapq.heappop(queue)
            if hops > jumps[i]:
                continue
            if i + 1 == n * n:
                return hops
            for j in range(i+1,min(i+7, n*n)):
                if hops+1 < jumps[flatten[j]]:
                    jumps[flatten[j]] = hops + 1
                    heapq.heappush(queue, (hops+1, flatten[j]))
        return - 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
        o = 4
        self.assertEqual(s.snakesAndLadders(i), o)

    def test_two(self):
        s = Solution()
        i = [[-1,-1],[-1,3]]
        o = 1
        self.assertEqual(s.snakesAndLadders(i), o)

    def test_three(self):
        s = Solution()
        i = [[2,4,-1],[8,-1,-1],[-1,6,-1]]
        o = 2
        self.assertEqual(s.snakesAndLadders(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,1,-1],[1,1,1],[-1,1,1]]
        o = -1
        self.assertEqual(s.snakesAndLadders(i), o)

    def test_five(self):
        s = Solution()
        i = [[-1,231,-1,173,-1,-1,46,39,30,-1,-1,-1,-1,-1,-1,172,-1],[287,-1,-1,-1,-1,-1,-1,-1,-1,66,-1,205,-1,28,-1,-1,-1],[141,-1,-1,-1,43,-1,-1,200,-1,-1,-1,147,-1,224,-1,-1,-1],[215,89,231,80,12,214,25,-1,-1,-1,-1,-1,281,-1,133,237,-1],[-1,-1,-1,-1,55,-1,177,172,-1,-1,-1,-1,-1,284,229,-1,-1],[-1,45,112,-1,-1,33,-1,-1,-1,-1,-1,-1,-1,-1,-1,178,266],[-1,128,-1,-1,191,219,-1,140,-1,-1,-1,-1,-1,-1,141,-1,-1],[-1,105,-1,-1,-1,-1,-1,173,-1,-1,-1,-1,-1,-1,-1,181,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,78,219,-1,56,-1,117,-1,-1,88,-1,44,103,-1,243],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,233,-1,218,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[201,136,-1,-1,-1,-1,-1,-1,-1,-1,-1,184,68,-1,-1,107,-1],[-1,-1,-1,-1,-1,185,-1,-1,-1,-1,52,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,52,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        o = 12
        self.assertEqual(s.snakesAndLadders(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)