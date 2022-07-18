# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List
from itertools import accumulate

class Solution:
    '''
    Given a matrix and a target, return the number of non-empty
    submatrices that sum to target.

    A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with
    x1 <= x <= x2 and y1 <= y <= y2.

    Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are
    different if they have some coordinate that is different: for
    example if x1 != x1'.
    '''
    # time limit exceeded (35/40 test cases)
    def numSubmatrixSumTarget_tle(self, matrix: List[List[int]], target: int) -> int:
        # dimensions of matrix
        m, n = len(matrix), len(matrix[0])
        # 2d prefix sum of matrix
        prefix = [list(accumulate(r)) for r in matrix]
        for i in range(1, m):
            for j in range(n):
                prefix[i][j] += prefix[i-1][j]
        # lookup of submatrix sum
        def s(a,b,c,d):
            v = prefix[c][d]
            if a > 0 and b > 0:
                v += prefix[a-1][b-1]
            if a > 0:
                v -= prefix[a-1][d]
            if b > 0:
                v -= prefix[c][b-1]
            return v
        # brute force check every submatrix
        answer = 0
        for a in range(m):
            for b in range(n):
                for c in range(a,m):
                    for d in range(b,n):
                        if s(a,b,c,d) == target:
                            answer += 1
        return answer

    # based on discussion post by sgallivan
    # https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/1162767/JS-Python-Java-C%2B%2B-or-Short-Prefix-Sum-Solution-w-Explanation
    # makes use of sliding window from a start column to end column in
    # rows (instead of brute force finding all submatrices)
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # dimensions of matrix
        m, n = len(matrix), len(matrix[0])
        # prefix sum rows of matrix
        prefix = [list(accumulate(r)) for r in matrix]
        # make use of a sliding window
        answer = 0
        # start column
        for i in range(n):
            # end column
            for j in range(i,n):
                counts = {0:1}
                running = 0
                for row in prefix:
                    running += row[j] - (row[i-1] if i else 0)
                    if running - target in counts:
                        answer += counts[running - target]
                    counts[running] = counts[running] + 1 if running in counts else 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,0],[1,1,1],[0,1,0]]
        j = 0
        o = 4
        self.assertEqual(s.numSubmatrixSumTarget(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,-1],[-1,1]]
        j = 0
        o = 5
        self.assertEqual(s.numSubmatrixSumTarget(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[904]]
        j = 0
        o = 0
        self.assertEqual(s.numSubmatrixSumTarget(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)