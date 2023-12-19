# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An image smoother is a filter of the size 3 x 3 that can be applied to each
    cell of an image by rounding down the average of the cell and the eight
    surrounding cells. If one or more of the surrounding cells of a cell is not
    present, it is not considered in the average.

    Given an m x n integer matrix img representing the grayscale of an image,
    return the image after applying the smoother on each cell of it.
    '''
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img), len(img[0])
        def convolve(i,j):
            s,c = 0,0
            for x in range(max(0, i-1), min(m, i+2)):
                for y in range(max(0, j-1), min(n, j+2)):
                    c += 1
                    s += img[x][y]
            return s // c
        return [[convolve(i,j) for j in range(n)] for i in range(m)]
    
class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,1],[1,0,1],[1,1,1]]
        o = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(s.imageSmoother(i), o)

    def test_two(self):
        s = Solution()
        i = [[100,200,100],[200,50,200],[100,200,100]]
        o = [[137,141,137],[141,138,141],[137,141,137]]
        self.assertEqual(s.imageSmoother(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)