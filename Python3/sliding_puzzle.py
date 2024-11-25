# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional, Tuple

class Solution:
    '''
    On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty
    square represented by 0. A move consists of choosing 0 and a 4-directionally
    adjacent number and swapping it.

    The state of the board is solved if and only if the board is
    [[1,2,3],[4,5,0]].

    Given the puzzle board board, return the least number of moves required so
    that the state of the board is solved. If it is impossible for the state of
    the board to be solved, return -1.
    '''
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def swap(state: Tuple[int]):
            states = []
            # [0,1,2]
            # [3,4,5]
            g = [[1,3],[0,2,4],[1,5],[0,4],[3,1,5],[2,4]]
            i = state.index(0)
            for j in g[i]:
                l = list(state)
                l[i],l[j] = l[j],l[i]
                states.append(tuple(l))
            return states
        target = tuple([1,2,3,4,5,0])
        visited = set()
        queue = deque([(tuple(board[0] + board[1]),0)])
        while queue:
            n,m = queue.popleft()
            if n in visited:
                continue
            visited.add(n)
            if n == target:
                return m
            for s in swap(n):
                if s not in visited:
                    queue.append((s,m+1))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[4,0,5]]
        o = 1
        self.assertEqual(s.slidingPuzzle(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3],[5,4,0]]
        o = -1
        self.assertEqual(s.slidingPuzzle(i), o)

    def test_three(self):
        s = Solution()
        i = [[4,1,2],[5,0,3]]
        o = 5
        self.assertEqual(s.slidingPuzzle(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)