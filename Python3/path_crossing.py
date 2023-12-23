# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing
    moving one unit north, south, east, or west, respectively. The starting
    position is the origin (0, 0) on a 2D plan and following the path.

    Return true if the path crosses itself at any point, that is, if at any time
    a location is visited again. Return false otherwise.
    '''
    def isPathCrossing(self, path: str) -> bool:
        s = {(0,0)}
        x,y = 0,0
        for p in path:
            if p == 'N':
                y += 1
            elif p == 'E':
                x += 1
            elif p == 'S':
                y -= 1
            else:
                x -= 1
            if (x,y) in s:
                return True
            s.add((x,y))
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "NES"
        o = False
        self.assertEqual(s.isPathCrossing(i), o)

    def test_two(self):
        s = Solution()
        i = "NESWW"
        o = True
        self.assertEqual(s.isPathCrossing(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)