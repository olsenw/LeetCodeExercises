# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed 2D integer matrix grid of size n * n. A 0-indexed 2D
    matrix of size n * m is defined as the product matrix of grid if the
    following condition is met:
    * Each element p[i][j] is calculated as the product of all elements in grid
      except for the element grid[i][j]. This product is then taken modulo
      12345.
    
    Return the product matrix of grid.
    '''
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        def modMul(a:int,b:int,mod:int=12345) -> int:
            return ((a % mod) * (b % mod)) % mod
        m,n = len(grid),len(grid[0])

        answer = [[1] * n for _ in range(m)]

        rowRight:List[List[int]] = []
        rowLeft:List[List[int]] = []
        for i in range(m):
            rowRight.append([1])
            rowLeft.append([1])
            right = 1
            left = 1
            for j in range(n):
                right = modMul(right,grid[i][j])
                rowRight[-1].append(right)
            for j in range(n-1,-1,-1):
                left = modMul(left,grid[i][j])
                rowLeft[-1].append(left)
            rowRight[-1].append(1)
            rowLeft[-1].append(1)
            rowLeft[-1] = rowLeft[-1][::-1]
        colUp = [1]
        colDown = [1]
        up = 1
        down = 1
        for i in range(m):
            down = modMul(down, rowRight[i][-2])
            colDown.append(down)
        for i in range(m-1,-1,-1):
            up = modMul(up, rowRight[i][-2])
            colUp.append(up)
        colUp.append(1)
        colUp = colUp[::-1]
        colDown.append(1)

        for i in range(m):
            for j in range(n):
                a = modMul(rowRight[i][j],rowLeft[i][j+2])
                b = modMul(colDown[i],colUp[i+2])
                answer[i][j] = modMul(a,b)

        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[3,4]]
        o = [[24,12],[8,6]]
        self.assertEqual(s.constructProductMatrix(i), o)

    def test_two(self):
        s = Solution()
        i = [[12345],[2],[1]]
        o = [[2],[0],[0]]
        self.assertEqual(s.constructProductMatrix(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)