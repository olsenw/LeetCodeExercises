# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import deque

class Solution:
    '''
    Given an m x n integers matrix, return the length of the longest
    increasing path in the matrix.

    From each cell you can either move in four directions: left, right,
    up, down. It is impossible to move diagonally or outside the outside
    of the boundaries of the matrix.
    '''
    # Topological Sorting
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        def links(x,y):
            if x > 0 and matrix[x-1][y] < matrix[x][y]:
                yield [x-1,y]
            if x < m - 1 and matrix[x+1][y] < matrix[x][y]:
                yield [x+1,y]
            if y > 0 and matrix[x][y-1] < matrix[x][y]:
                yield [x,y-1]
            if y < n - 1 and matrix[x][y+1] < matrix[x][y]:
                yield [x,y+1]
        order = sorted([(matrix[i][j], i, j) for i in range(m) for j in range(n)], reverse=True)
        dp = [[0] * n for _ in range(m)]
        for _, i, j in order:
            if not dp[i][j]:
                dp[i][j] = 1
                s = deque([[i,j]])
                while s:
                    x, y = s.popleft()
                    for a, b in links(x,y):
                        if dp[a][b] < dp[x][y] + 1:
                            dp[a][b] = dp[x][y] + 1
                            s.append([a,b])
        return max(max(i) for i in dp)
    
    # better dp solution by meaditya (saved here for reference)
    # https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/2052360/Python%3A-Beginner-Friendly-%22Recursion-to-DP%22-Intuition-Explained
    # my solution goes from largest value to smallest value, this means
    # that the dp array could be overwritten many times when a better
    # path is found. meaditya instead starts at small number and works
    # up meaning once a value has been recursively found it will not 
    # need to be updated again.
    def longestIncreasingPath_meaditya(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # create a dp array of size m * n to store already computed max_increasing_path_length for index (i, j)
        # where 0 <= i < m and 0 <= j < n
        # initialize the dp array by -1 as length of path can only be a whole number. 
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
                return 0
            
            # if dp[i][j] != -1, that means dp[i][j] has been updated by some >= 0 path length.
            # hence directly use it without recomputing and save recursion time and space.
            if dp[i][j] != -1:
                return dp[i][j]
            
            # compute if dp[i][j] = -1 meaning (i, j) still not computed
            left = dfs(i, j - 1, matrix[i][j])
            right = dfs(i, j + 1, matrix[i][j])
            top = dfs(i - 1, j, matrix[i][j])
            bottom = dfs(i + 1, j, matrix[i][j])
            
            # update the dp value after computing path length for index (i , j)
            # so that we can use it next time without recomputation.
            dp[i][j] = max(left, right, top, bottom) + 1
            return dp[i][j]
        
        ans = -1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -1))
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[9,9,4],[6,6,8],[2,1,1]]
        o = 4
        self.assertEqual(s.longestIncreasingPath(i), o)

    def test_two(self):
        s = Solution()
        i = [[3,4,5],[3,2,6],[2,2,1]]
        o = 4
        self.assertEqual(s.longestIncreasingPath(i), o)

    def test_three(self):
        s = Solution()
        i = [[1]]
        o = 1
        self.assertEqual(s.longestIncreasingPath(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)