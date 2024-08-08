# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Start at the cell (rStart, cStart) or an rows x cols grid facing east. The
    northwest corner is at the first row and column in the grid, and the
    southeast corner is at the last row and column.

    Walk a clockwise spiral shape to visit every position in this grid. Whenever
    the grid boundary is left, it is possible to continue walking and return to
    the grid later. Eventually, all rows * cols spaces of the grid will be
    visited.

    Return an array of coordinates representing the positions of the grid in the
    order visited.
    '''
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        answer = []
        x,y = rStart, cStart
        # 0 = right, 1 = down, 2 = left, 3 = up
        d = 0
        i = 1
        t = cStart + i
        while len(answer) < rows * cols:
            # answer.append([x,y])
            if 0 <= x < rows and 0 <= y < cols:
                answer.append([x,y])
            if d == 0:
                y += 1
                if y == t:
                    d += 1
                    t = x + i
            elif d == 1:
                x += 1
                if x == t:
                    d += 1
                    i += 1
                    t = y - i
            elif d == 2:
                y -= 1
                if y == t:
                    d += 1
                    t = x - i
            elif d == 3:
                x -= 1
                if x == t:
                    d = 0
                    i += 1
                    t = y + i
            else:
                raise ValueError("oops direction invalid")
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1, 4, 0, 0
        o = [[0,0],[0,1],[0,2],[0,3]]
        self.assertEqual(s.spiralMatrixIII(*i), o)

    def test_two(self):
        s = Solution()
        i = 5, 6, 1, 4
        o = [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
        self.assertEqual(s.spiralMatrixIII(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)