# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed n x n integer matrix grid, return the number of pairs
    (ri, ci) such that row r1 and column c1 are equal.

    A row and column pair is considered equal if they contain the same elements
    in the same order (ie, an equal array).
    '''
    # slow... probably only works because n <= 200
    def equalPairs_passes(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def compare(i,j):
            for k in range(n):
                if grid[i][k] != grid[k][j]:
                    return False
            return True
        d = dict()
        for i,j in enumerate(grid[0]):
            if j in d:
                d[j].append(i)
            else:
                d[j] = [i]
        answer = 0
        for i in range(n):
            if grid[i][0] in d:
                for j in d[grid[i][0]]:
                    if compare(i,j):
                        answer += 1
        return answer

    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = Counter(tuple(r) for r in grid)
        col = Counter(tuple(grid[i][c] for i in range(n)) for c in range(n))
        answer = 0
        for r in row:
            if r in col:
                answer += row[r] * col[r]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[3,2,1],[1,7,6],[2,7,7]]
        o = 1
        self.assertEqual(s.equalPairs(i), o)

    def test_two(self):
        s = Solution()
        i = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
        o = 3
        self.assertEqual(s.equalPairs(i), o)

    def test_three(self):
        s = Solution()
        i = [[1]*200 for _ in range(200)]
        o = 200 * 200
        self.assertEqual(s.equalPairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)