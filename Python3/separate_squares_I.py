# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents
    the coordinates of the bottom-left point and the side length of a square
    parallel to the x-axis.

    Find the minimum y-coordinate value of a horizontal line such that the total
    area of the squares above the line equals the total area of the squares
    below the line.
    '''
    def separateSquares_incomplete(self, squares: List[List[int]]) -> float:
        squares = [(s[1],s[1]+s[2],s[2]*s[2]) for s in squares]
        totalArea = [0]
        for s in squares:
            totalArea.append(totalArea[-1] + s[2])
        i,j = 0, squares[-1][1]
        while j - i > 0.00001:
            k = (i + j) / 2
            l = bisect.bisect_left(squares, k, key=lambda x:x[0])
            r = bisect.bisect(squares, k, key=lambda x:x[1])
            pass
        return 1.0

    def separateSquares(self, squares: List[List[int]]) -> float:
        targetArea = sum(s[2]*s[2] for s in squares) / 2
        squares.sort(key=lambda x:(x[1],x[2]))
        # i,j = squares[0][0],squares[-1][1]+squares[-1][2]
        i,j = squares[0][0],max(s[1]+s[2] for s in squares)
        while j - i > 0.000001:
            k = (i + j) / 2
            a = 0
            for s in squares:
                if k < s[1] or a > targetArea:
                    break
                elif s[1] <= k < s[1] + s[2]:
                    a += (k - s[1]) * s[2]
                else:
                    a += s[2] * s[2]
            if a >= targetArea:
                j = k
            else:
                i = k
            pass
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0,1],[2,2,1]]
        o = 1.0
        self.assertAlmostEqual(s.separateSquares(i), o, 5)

    def test_two(self):
        s = Solution()
        i = [[0,0,2],[1,1,1]]
        o = 1.16667
        self.assertAlmostEqual(s.separateSquares(i), o, 5)

    def test_three(self):
        s = Solution()
        i = [[4,16,9],[1,16,2]]
        o = 20.27778
        self.assertAlmostEqual(s.separateSquares(i), o, 5)

    def test_four(self):
        s = Solution()
        i = [[8,16,1],[6,15,10]]
        o = 19.95
        self.assertAlmostEqual(s.separateSquares(i), o, 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)