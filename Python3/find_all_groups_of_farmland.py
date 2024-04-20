# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed m x n binary matrix land where a 0 represents a hectare of
    forested land and a 1 represents a hectare of farmland.

    To keep the land organized, there are designated rectangular areas of
    hectares that consist entirely of farmland. These rectangular areas are
    called groups. No two groups are adjacent, meaning farmland in one group is
    not four-directionally adjacent to another farmland in a different group.

    land can be represented by a coordinate system where the top left corner of
    land is (0,0) and the bottom right corner of land is (m-1,n-1). Find the
    coordinates of the top left and bottom right corner of each group of
    farmland. A group of farmland with a top left corner at (r1,c1) and a bottom
    right corner at (r2,c2) is represented by the 4-length array [r1,c1,r2,c2].

    Return a 2D array containing the 4-length arrays described above for each
    group of farmland in land. If there are no groups of farmland, return an
    empty array. Answer may be returned in any order.
    '''
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m,n = len(land), len(land[0])
        answer = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    for x in range(i,m):
                        if land[x][j] == 0:
                            x -= 1
                            break
                        for y in range(j, n):
                            if land[x][y] == 0:
                                y -= 1
                                break
                            land[x][y] = 0
                    answer.append([i,j,x,y])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0,0],[0,1,1],[0,1,1]]
        o = [[0,0,0,0],[1,1,2,2]]
        self.assertEqual(s.findFarmland(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[1,1]]
        o = [[0,0,1,1]]
        self.assertEqual(s.findFarmland(i), o)

    def test_three(self):
        s = Solution()
        i = [[0]]
        o = []
        self.assertEqual(s.findFarmland(i), o)

    def test_four(self):
        s = Solution()
        i = [[1]]
        o = [[0,0,0,0]]
        self.assertEqual(s.findFarmland(i), o)

    def test_five(self):
        s = Solution()
        i = [[0,0,0],[0,1,1],[0,1,1]]
        o = [[1,1,2,2]]
        self.assertEqual(s.findFarmland(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)