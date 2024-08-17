# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n integer matrix points (0-indexed). Starting with 0 points,
    maximize the number of points that can be obtained from the matrix.

    To gain points, pick one cell in each row. Picking the cell at coordinates
    (r,c) will add points[r][c] to the score.

    However, points will be lost if a next cell picked is to far from the cell
    in the previous row. For every two adjacent rows r and r + 1 
    (where 0 <= r < m - 1), picking cells at coordinates (r,c1) and (r+1,c2)
    will subtract abs(c1-c2) from the score.

    Return the maximum number of points that can be achieved.
    '''
    # brute force backtracking
    def maxPoints_tle(self, points: List[List[int]]) -> int:
        m,n = len(points), len(points[0])
        dp = [[0] * n for _ in range(m-1)]
        dp.append(points[-1])
        for i in range(m-2,-1,-1):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = max(dp[i][j], points[i][j] + dp[i+1][k] - abs(j - k))
        return max(dp[0])

    def maxPoints_tle2(self, points: List[List[int]]) -> int:
        m,n = len(points), len(points[0])
        @cache
        def dp(i,j):
            if i == 0:
                return points[0][j]
            return max(points[i][j] + dp(i-1, k) - abs(j-k) for k in range(n))
        return max(dp(m-1,k) for k in range(n))

    # inspiration from Leetcode editorial
    # https://leetcode.com/problems/maximum-number-of-points-with-cost/editorial/?envType=daily-question&envId=2024-08-17
    def maxPoints(self, points: List[List[int]]) -> int:
        m,n = len(points), len(points[0])
        prev = [p for p in points[0]]
        curr = [0] * n
        left = [0] * n
        right = [0] * n
        for i in range(1,m):
            curr = [0] * n
            left[0] = prev[0]
            for j in range(1,n):
                left[j] = max(left[j-1] - 1, prev[j])
            right[-1] = prev[-1]
            for j in range(n-2,-1,-1):
                right[j] = max(right[j+1] - 1, prev[j])
            for j in range(n):
                curr[j] = points[i][j] + max(left[j], right[j])
            prev = curr
        return max(prev)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[1,5,1],[3,1,1]]
        o = 9
        self.assertEqual(s.maxPoints(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,5],[2,3],[4,2]]
        o = 11
        self.assertEqual(s.maxPoints(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)