# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D binary array grid. Find 3 non-overlapping rectangles having
    non-zero areas with horizontal and vertical sides such that all the 1's in 
    grid lie inside these rectangles.

    Return the minimum possible sum of the area of these rectangles.

    Note that the rectangles are allowed to touch.
    '''
    # based on hints
    def minimumSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        # calculate the minimum area with upper left and lower right bounds
        def area(a,b,c,d) -> int:
            left,right = d,b
            up,down = c,a
            for i in range(a,c+1):
                for j in range(b,d+1):
                    if grid[i][j]:
                        left = min(left, j)
                        right = max(right, j)
                        up = min(up, i)
                        down = max(down, i)
            if down < up or right < left:
                return 0
            return (down - up + 1) * (right - left + 1)
        # find minimum area needed when split a region vertically
        def vertical(a,b,c,d) -> int:
            answer = m * n
            for j in range(b,d):
                left = area(a,b,c,j)
                right = area(a,j+1,c,d)
                if left and right:
                    answer = min(answer, left + right)
            return answer if answer < m * n else 0
        # find minimum area needed when split a region horizontally
        def horizontal(a,b,c,d) -> int:
            answer = m * n
            for i in range(a,c):
                up = area(a,b,i,d)
                down = area(i+1,b,c,d)
                if up and down:
                    answer = min(answer, up + down)
            return answer if answer < m * n else 0
        answer = m * n
        # split vertically
        for j in range(n-1):
            # split left region
            left = area(0,0,m-1,j)
            v = vertical(0,j+1,m-1,n-1)
            h = horizontal(0,j+1,m-1,n-1)
            if left and v:
                answer = min(answer, left + v)
            if left and h:
                answer = min(answer, left + h)
            # split right region
            right = area(0,j+1,m-1,n-1)
            v = vertical(0,0,m-1,j)
            h = horizontal(0,0,m-1,j)
            if right and v:
                answer = min(answer, right + v)
            if right and h:
                answer = min(answer, right + h)
        # split vertically
        for i in range(m-1):
            up = area(0,0,i,n-1)
            v = vertical(i+1,0,m-1,n-1)
            h = horizontal(i+1,0,m-1,n-1)
            if up and v:
                answer = min(answer, up + v)
            if up and h:
                answer = min(answer, up + h)
            down = area(i+1,0,m-1,n-1)
            v = vertical(0,0,i,n-1)
            h = horizontal(0,0,i,n-1)
            if down and v:
                answer = min(answer, down + v)
            if down and h:
                answer = min(answer, down + h)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0,1],[1,1,1]]
        o = 5
        self.assertEqual(s.minimumSum(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0,1,0],[0,1,0,1]]
        o = 5
        self.assertEqual(s.minimumSum(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,0,0],[0,0,0],[0,0,1],[1,1,0]]
        o = 3
        self.assertEqual(s.minimumSum(i), o)

    def test_four(self):
        s = Solution()
        i = [[0,0,0],[0,0,0],[0,1,1],[0,1,0]]
        o = 3
        self.assertEqual(s.minimumSum(i), o)

    def test_five(self):
        s = Solution()
        i = [[0,0,0,1],[0,0,0,1],[0,0,0,1]]
        o = 3
        self.assertEqual(s.minimumSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)