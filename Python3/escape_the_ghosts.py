# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a simplified PAC-MAN game on an infinite 2-D grid. PAC-MAN starts
    at the point [0,0], and has a destination point target = [xtarget, ytarget]
    that they are trying to get to. There are several ghosts on the map with
    their starting positions given as a 2D array ghosts, where
    ghosts[i] = [xi,yi] represents the starting position of the ith ghost. All
    inputs are integral coordinates.

    Each turn PAC-MAN and the ghosts may independently choose to either move 1
    unit in any of the four cardinal directions: north, east, south, or west, or
    stay still. All actions happen simultaneously.

    PAC-MAN escapes if and only if they can reach the target before any ghost
    reaches them. If PAC-MAN reaches any square at the same time as a ghost, it
    does not count as an escape.

    Return true if it is possible to escape regardless of how the ghosts move,
    otherwise return false.
    '''
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def time(a:int,b:int) -> int:
            return abs(target[0] - a) + abs(target[1] - b)
        pacman = time(0,0)
        for a,b in ghosts:
            if time(a,b) <= pacman:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0],[0,3]]
        j = [0,1]
        o = True
        self.assertEqual(s.escapeGhosts(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,0]]
        j = [2,0]
        o = False
        self.assertEqual(s.escapeGhosts(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[2,0]]
        j = [1,0]
        o = False
        self.assertEqual(s.escapeGhosts(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)