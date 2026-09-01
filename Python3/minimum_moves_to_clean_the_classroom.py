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
    Given an m x n grid classroom where a student volunteer is tasked with
    cleaning up litter scattered around the room. Each cell in the grid is one
    of the following:
    * 'S': Starting position of the student
    * 'L': Litter that must be collected (once collected, the cell becomes
      empty)
    * 'R': Reset area that restores the student's energy to full capacity,
      regardless of their current energy level (can be used multiple times)
    * 'X': Obstacle the student cannot pass through
    * '.': Empty space

    Also given an integer energy, representing the student's maximum energy
    capacity. The student starts with this energy from the starting position
    'S'.

    Each move to an adjacent cell (up, down, left, or right) costs 1 unit of
    energy. If the energy reaches 0, the student can only continue if they are
    on a reset area 'R', which resets the energy to its maximum capacity energy.

    Return the minimum number of moves required to collect all litter items, or
    -1 if it's impossible.
    '''
    def minMoves_tle(self, classroom: List[str], energy: int) -> int:
        m,n = len(classroom), len(classroom[0])
        x,y = 0,0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    x,y = i,j
        litter = sum(c.count('L') for c in classroom)
        # tuple(moves, energy remaining, position x, position y, litter collected)
        heap = [(0,energy,x,y,set())]
        while heap:
            moves, remEnergy, x, y, collected = heapq.heappop(heap)
            if moves > m * n:
                continue
            if classroom[x][y] == 'L' and (x,y) not in collected:
                collected.add((x,y))
            if len(collected) == litter:
                return moves
            if classroom[x][y] == 'R':
                remEnergy = energy
            if remEnergy == 0:
                continue
            for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= a < m and 0 <= b < n and classroom[a][b] != 'X':
                    heapq.heappush(heap, (moves+1,remEnergy-1,a,b,set(collected)))
        return -1

    # based on hints
    # important note: there is at most 10 'L' (can use bitmask to store)
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m,n = len(classroom),len(classroom[0])
        sx,sy = 0,0
        # dictionary position (x,y) -> unique litter mask
        litterDict = dict()
        litterTotal = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx,sy = i,j
                if classroom[i][j] == 'L':
                    litterDict[(i,j)] = 1 << len(litterDict)
                    litterTotal |= litterDict[(i,j)]
        # track largest energy seen for (x,y,mask)
        # prune bfs paths that are less than best seen
        bestEnergy = defaultdict(int)
        # BFS
        # position x, position y, litter mask, remaining energy, total moves
        # heap = [(sx,sy,0,energy,0)]
        # total moves, remaining energy, position x, position y, litter mask
        heap = [(0,energy,sx,sy,0)]
        while heap:
            # x,y,mask,remEnergy,moves = heapq.heappop(heap)
            moves,remEnergy,x,y,mask = heapq.heappop(heap)
            if classroom[x][y] == 'L':
                mask |= litterDict[(x,y)]
            if mask == litterTotal:
                return moves
            if classroom[x][y] == 'R':
                remEnergy = energy
            if remEnergy == 0:
                continue
            if remEnergy <= bestEnergy[(x,y,mask)]:
                continue
            else:
                bestEnergy[(x,y,mask)] = remEnergy
            for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= a < m and 0 <= b < n and classroom[a][b] != 'X':
                    # heapq.heappush(heap, (a,b,mask,remEnergy-1,moves+1))
                    heapq.heappush(heap, (moves+1,remEnergy-1,a,b,mask))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["S.", "XL"]
        j = 2
        o = 2
        self.assertEqual(s.minMoves(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["LS", "RL"]
        j = 4
        o = 3
        self.assertEqual(s.minMoves(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["L.S", "RXL"]
        j = 3
        o = -1
        self.assertEqual(s.minMoves(i,j), o)

    def test_four(self):
        s = Solution()
        i = ["RRL.", "LSXX", "RL.L", "LLL.", "L..."]
        j = 15
        o = 14
        self.assertEqual(s.minMoves(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)