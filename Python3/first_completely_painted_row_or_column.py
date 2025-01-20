# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array arr, and an m x n integer matrix mat. arr
    and mat both contain all the integers in the range [1, m * n].

    Go through each index i in arr starting from index 0 and paint the cell in
    mat containing the integer arr[i].

    Return the smallest index i at which either a row or a column will be
    completely painted in mat.
    '''
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        d = dict()
        r = {i:set() for i in range(m)}
        c = {i:set() for i in range(n)}
        for i in range(m):
            for j in range(n):
                d[mat[i][j]] = (i,j)
                r[i].add(mat[i][j])
                c[j].add(mat[i][j])
        for i in range(len(arr)):
            a,b = d[arr[i]]
            r[a].remove(arr[i])
            c[b].remove(arr[i])
            if len(r[a]) == 0 or len(c[b]) == 0:
                return i
        return len(arr)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,4,2]
        j = [[1,4],[2,3]]
        o = 2
        self.assertEqual(s.firstCompleteIndex(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,8,7,4,1,3,5,6,9]
        j = [[3,2,5],[1,4,6],[8,7,9]]
        o = 3
        self.assertEqual(s.firstCompleteIndex(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)