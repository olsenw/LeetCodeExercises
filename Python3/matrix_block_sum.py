# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a m x n matrix mat and an integer k, return a matrix answer where each
    answer[i][j] is the sum of all elements mat[r][c] for:
    * i - k <= r <= i + k
    * j - k <= c <= j + k
    * (r,c) is a valid position in the matrix
    '''
    # brute force
    def matrixBlockSum_tle(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        answer = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for r in range(i - k, i + k + 1):
                    if 0 <= r < m:
                        for c in range(j - k, j + k + 1):
                            if 0 <= c < n:
                                answer[i][j] += mat[r][c]
        return answer

    def matrixBlockSum_incorrect(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        answer = [[mat[i][j] for j in range(n)] for i in range(m)]
        width = [[mat[i][j] for j in range(n)] for i in range(m)]
        height = [[mat[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(1,n):
                width[i][j] = width[i][j-1] + mat[i][j]
        for i in range(1,m):
            for j in range(n):
                height[i][j] = height[i-1][j] + mat[i][j]
        for i in range(m):
            a,b = max(i-k, 0), min(i+k, m-1)
            for j in range(n):
                x,y = max(j-k, 0), min(j+k, m-1)
                answer[i][j] += width[i][y] - width[i][x] + mat[i][x]
                answer[i][j] += height[b][j] - height[a][j] + mat[a][j]
        return answer

    # based on hints
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        answer = [[mat[i][j] for j in range(n)] for i in range(m)]
        dp = [[mat[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(1,n):
                dp[i][j] += dp[i][j-1]
        for i in range(1,m):
            for j in range(n):
                dp[i][j] += dp[i-1][j]
        for i in range(m):
            a,b = max(i-k, 0), min(i+k, m-1)
            for j in range(n):
                x,y = max(j-k, 0), min(j+k, n-1)
                answer[i][j] = dp[b][y]
                if a-1 >= 0:
                    answer[i][j] -= dp[a-1][y]
                if x-1 >= 0:
                    answer[i][j] -= dp[b][x-1]
                if a-1 >= 0 and x-1 >= 0:
                    answer[i][j] += dp[a-1][x-1]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],
             [4,5,6],
             [7,8,9]]
        j = 1
        o = [[12,21,16],[27,45,33],[24,39,28]]
        self.assertEqual(s.matrixBlockSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        j = 2
        o = [[45,45,45],[45,45,45],[45,45,45]]
        self.assertEqual(s.matrixBlockSum(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]]
        j = 3
        o = [[731,731,731],[930,930,930],[930,930,930],[930,930,930],[721,721,721]]
        self.assertEqual(s.matrixBlockSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)