# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an mxn binary matrix filled with 0's and 1's find the largets
    square containing only 1's and return its area.
    '''
    def maximalSquareBrute(self, matrix: List[List[str]]) -> int:
        k = 0
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        while i < m:
            j = 0
            while j < n:
                if i + k >= m: # check if out of bounds
                    break
                if j + k >= n: # check if out of bounds
                    break
                for ii in range(i, i+k+1):
                    for jj in range(j, j+k+1):
                        if matrix[ii][jj] == "0":
                            break
                    else: # neat way to break nested loops python
                        continue # only runs if for not broken out of
                    break
                else:
                    k += 1
                    j -= 1
                j += 1
            i += 1
        return k*k

    '''
    Dynamic programing solution using 2d array
    Based on solution description from leetcode
    '''
    def maximalSquareDP2D(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        area = 0
        # dynamic programing array same size as input
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        # note starts to ensure within bounds
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1": # only care about 1's
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    area = max(area, dp[i][j])
        return area * area

    '''
    Dynamic programing solution using 1d array
    Based on solution description from leetcode

    $ = prev, # = dp[i:], 0 = dp[:i-1], @ = dp[i] (ie considered/update) 

    **$###
    000@**
    ******
    '''
    def maximalSquareDP1D(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        area = 0
        # dynamic programing array same size as input
        prev = 0
        dp = [0 for j in range(n+1)]
        # note starts to ensure within bounds
        for i in range(1, m+1):
            for j in range(1, n+1):
                temp = dp[j]
                if matrix[i-1][j-1] == "1": # only care about 1's
                    dp[j] = min(dp[j-1], dp[j], prev) + 1
                    area = max(area, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return area * area

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        a = 4
        self.assertEqual(s.maximalSquareBrute(m), a)
        self.assertEqual(s.maximalSquareDP2D(m), a)
        self.assertEqual(s.maximalSquareDP1D(m), a)

    def test_two(self):
        s = Solution()
        m = [["0","1"],["1","0"]]
        a = 1
        self.assertEqual(s.maximalSquareBrute(m), a)
        self.assertEqual(s.maximalSquareDP2D(m), a)
        self.assertEqual(s.maximalSquareDP1D(m), a)

    def test_three(self):
        s = Solution()
        m = [["0"]]
        a = 0
        self.assertEqual(s.maximalSquareBrute(m), a)
        self.assertEqual(s.maximalSquareDP2D(m), a)
        self.assertEqual(s.maximalSquareDP1D(m), a)

    def test_four(self):
        s = Solution()
        m = [["1","1"],["1","1"]]
        a = 4
        self.assertEqual(s.maximalSquareBrute(m), a)
        self.assertEqual(s.maximalSquareDP2D(m), a)
        self.assertEqual(s.maximalSquareDP1D(m), a)

    def test_five(self):
        s = Solution()
        m = [["1","1"]]
        a = 1
        self.assertEqual(s.maximalSquareBrute(m), a)
        self.assertEqual(s.maximalSquareDP2D(m), a)
        self.assertEqual(s.maximalSquareDP1D(m), a)

    def test_six(self):
        s = Solution()
        m = [["1","1","1","1","1"],["1","1","1","1","1"],["0","0","0","0","0"],["1","1","1","1","1"],["1","1","1","1","1"]]
        a = 4
        self.assertEqual(s.maximalSquareBrute(m), a)
        self.assertEqual(s.maximalSquareDP2D(m), a)
        self.assertEqual(s.maximalSquareDP1D(m), a)

if __name__ == '__main__':
    unittest.main(verbosity=2)