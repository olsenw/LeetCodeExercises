# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an image represented by an m x n grid of integers image, where
    image[i][j] represents the pixel value of the image. Also given are three
    integers sr, sc, and color. Perform the flood fill operation on the image
    starting from the pixel image[sr][sc].

    To perform a flood fill:
    1. Begin with the starting pixel and change its color to color.
    2. Perform the same process for each pixel that is directly adjacent (pixels
       that share a side with the original pixel, either horizontally or
       vertically) and shares the same color as the starting pixel.
    3. Keep repeating this process by checking neighboring pixels of the updated
       pixels and modifying their color if it matches the original color of the
       starting pixel.
    4. The process stops when there are no more adjacent pixels of the original
       color to update.
    
    Return the modified image after performing the flood fill.
    '''
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image), len(image[0])
        visited = set()
        target = image[sr][sc]
        image[sr][sc] = color
        queue = deque([(sr,sc)])
        while queue:
            x,y = queue.popleft()
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= i < m and 0 <= j < n and image[i][j] == target:
                    image[i][j] = color
                    queue.append((i,j))
        return image

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,1],[1,1,0],[1,0,1]]
        j = 1
        k = 1
        l = 2
        o = [[2,2,2],[2,2,0],[2,0,1]]
        # self.assertEqual(s.floodFill(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = [[0,0,0],[0,0,0]]
        j = 0
        k = 0
        l = 0
        o = [[0,0,0],[0,0,0]]
        self.assertEqual(s.floodFill(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)