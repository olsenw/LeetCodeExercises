# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n integer matrix grid, where m and n are both even integers,
    and an integer k.

    The matrix is composed of several layers, which is shown in the below image,
    where each color is its own layer:
    (Image online)

    A cyclic rotation of the matrix is done by cyclically rotating each layer in
    the matrix. To cyclically rotate a layer once, each element in the layer
    will take the place of the adjacent element in the counter-clockwise
    direction.

    Return the matrix after applying k cyclic rotations to it.
    '''
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        for layer in range(min(m,n)//2):
            values = []
            # West
            for i in range(layer,m-layer):
                values.append(grid[i][layer])
            # South
            for j in range(layer+1,n-layer):
                values.append(grid[m-layer-1][j])
            # East
            for i in range(m-layer-2,layer,-1):
                values.append(grid[i][n-layer-1])
            # North
            for j in range(n-layer-1,layer,-1):
                values.append(grid[layer][j])
            # Rotate by k
            index = (len(values) - (k % len(values))) % len(values)
            # West
            for i in range(layer,m-layer):
                grid[i][layer] = values[index]
                index = index + 1 if index + 1 < len(values) else 0
            # South
            for j in range(layer+1,n-layer):
                grid[m-layer-1][j] = values[index]
                index = index + 1 if index + 1 < len(values) else 0
            # East
            for i in range(m-layer-2,layer-1,-1):
                grid[i][n-layer-1] = values[index]
                index = index + 1 if index + 1 < len(values) else 0
            # North
            for j in range(n-layer-2,layer,-1):
                grid[layer][j] = values[index]
                index = index + 1 if index + 1 < len(values) else 0
        return grid

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[40,10],[30,20]]
        j = 1
        o = [[10,20],[40,30]]
        self.assertEqual(s.rotateGrid(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        j = 2
        o = [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
        self.assertEqual(s.rotateGrid(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[70,1,10,20],[60,50,40,30]]
        j = 6
        o = [[50,60,70,1],[40,30,20,10]]
        self.assertEqual(s.rotateGrid(i,j), o)

    def test_four(self):
        s = Solution()
        i = [[70,1,10,20],[60,50,40,30]]
        j = 16
        o = [[70,1,10,20],[60,50,40,30]]
        self.assertEqual(s.rotateGrid(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)