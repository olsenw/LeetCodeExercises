# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n binary matrix mat, return the number of sub matrices that
    have all ones.
    '''
    # brute force (m^2 n^2)
    def numSubmat_brute_fail(self, mat: List[List[int]]) -> int:
        answer = 0
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                pass
                k = n
                for a in range(i,m):
                    if mat[a][j] == 0:
                        break
                    for b in range(j,k):
                        if mat[a][b] == 0:
                            k = b
                            break
                    answer += (a - i + 1) * (k - j)
        return answer
    
    # brute force (barely passes)
    # probably not the intended solution
    def numSubmat_(self, mat: List[List[int]]) -> int:
        answer = 0
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                pass
                k = n
                for a in range(i,m):
                    if mat[a][j] == 0:
                        break
                    for b in range(j,k):
                        if mat[a][b] == 0:
                            k = b
                            break
                    answer += (k - j)
        return answer

    '''
    better solutions exist where count all rect that have bottom right at i,j
    and an array to track heights

    monotonic stack solution is real good for tracking heights and counting
    '''
    # based on LeetCode monotonic solution
    # https://leetcode.com/problems/count-submatrices-with-all-ones/?envType=daily-question&envId=2025-08-21
    def numSubmat_leetcode_monotonic(self, mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        # used to track the max height of 1's for given column
        heights = [0] * n
        answer = 0
        for i in range(m):
            # update heights with row i as bottom row
            for j in range(n):
                heights[j] = 0 if mat[i][j] == 0 else heights[j] + 1
            # monotonic stack
            # find nearest smaller height to column height j
            stack = [[-1,0,-1]]
            for j in range(n):
                # current element is bigger than height at column j
                while stack[-1][2] >= heights[j]:
                    stack.pop()
                # get last smaller column
                k, prev, _ = stack[-1]
                # update count with new possible rectangles
                # (ie now possible with higher height and end bottom right)
                cur = prev + (j - k) * heights[j]
                # add current column to stack
                stack.append([j, cur, heights[j]])
                answer += cur
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0,1],[1,1,0],[1,1,0]]
        o = 13
        self.assertEqual(s.numSubmat(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
        o = 24
        self.assertEqual(s.numSubmat(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)