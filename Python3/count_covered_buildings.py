# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n, representing an n x n city. Also given a 2D grid
    buildings, where buildings[i] = [x, y] denotes a unique building located at
    coordinates [x, y].

    A building is covered if there is at least one building in all four
    directions: left, right, above, and below.

    Return the number of covered buildings.
    '''
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        up = [0] * (n+1)
        down = [n+1] * (n+1)
        left = [n+1] * (n+1)
        right = [0] * (n+1)
        answer = 0
        for x,y in buildings:
            up[x] = max(y, up[x])
            down[x] = min(y, down[x])
            left[y] = min(x, left[y])
            right[y] = max(x, right[y])
        for x,y in buildings:
            if down[x] < y < up[x] and left[y] < x < right[y]:
                answer += 1 
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[1,2],[2,2],[3,2],[2,1],[2,3]]
        o = 1
        self.assertEqual(s.countCoveredBuildings(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [[1,1],[1,2],[2,1],[2,2]]
        o = 0
        self.assertEqual(s.countCoveredBuildings(i,j), o)

    def test_three(self):
        s = Solution()
        i = 5
        j = [[1,3],[3,2],[3,3],[3,5],[5,3]]
        o = 1
        self.assertEqual(s.countCoveredBuildings(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)