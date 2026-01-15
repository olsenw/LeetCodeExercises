# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers, n and m and two integer arrays, hBars and vBars. The
    grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit
    cells. The bars are indexed starting from 1.

    It is possible to remove some of the bars in hBars from horizontal bars and
    some of the bars in vBars from vertical bars. Note that other bars are fixed
    and cannot be removed.

    Return an integer denoting the maximum area of a square shaped hold in the
    grid, after removing some bars (possibly none).
    '''
    # based on hints
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        hx,hy = hBars[0],hBars[0]
        last = hBars[0]
        start = hBars[0]
        for h in hBars:
            if last + 1 == h:
                last = h
            else:
                if last - start > hy - hx:
                    hx = start
                    hy = last
                last = h
                start = h
        if last - start > hy - hx:
            hx = start
            hy = last
        
        vx,vy = vBars[0],vBars[0]
        last = vBars[0]
        start = vBars[0]
        for v in vBars:
            if last + 1 == v:
                last = v
            else:
                if last - start > vy - vx:
                    vx = start
                    vy = last
                last = v
                start = v
        if last - start > vy - vx:
            vx = start
            vy = last
        
        a = min(hy - hx + 2, vy - vx + 2)

        return a * a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = 1
        k = [2,3]
        l = [2]
        o = 4
        self.assertEqual(s.maximizeSquareHoleArea(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 1
        j = 1
        k = [2]
        l = [2]
        o = 4
        self.assertEqual(s.maximizeSquareHoleArea(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        i = 2
        j = 3
        k = [2,3]
        l = [2,4]
        o = 4
        self.assertEqual(s.maximizeSquareHoleArea(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)