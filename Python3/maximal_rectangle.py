# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a rows x cols binary matrix filled with 0's and 1's, find the largest
    rectangle containing only 1's and return its area.
    '''
    # O((m*n)^2) time
    def maximalRectangle_brute(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix), len(matrix[0])
        def blob(a,b):
            answer = 1
            right = n
            for i in range(a, m):
                if matrix[i][b] == '0':
                    break
                for j in range(b, min(right, n)):
                    if matrix[i][j] == '0':
                        right = j
                        break
                    answer = max(answer, (i - a + 1) * (j - b + 1))
            return answer
        answer = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    answer = max(answer, blob(i,j))
        return answer

    def maximalRectangle_unfinished(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix), len(matrix[0])
        answer = 0
        dp = [list(range(n+1)) for _ in range(m)]
        for i in range(m):
            for j in range(n-1,-1,-1):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i][j+1]
        return answer

    # monotonic stack based on solution by anwendeng
    # https://leetcode.com/problems/maximal-rectangle/solutions/5014468/monotonic-stack-count-successive-1-s-16ms-beats-99-62/?envType=daily-question&envId=2024-04-13
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix), len(matrix[0])
        answer = 0
        h = [0] * (n+1)
        for i in range(m):
            s = []
            for j in range(n+1):
                if j == n or matrix[i][j] == '0':
                    h[j] = 0
                else:
                    h[j] = h[j]+1
                # monotonic stack
                while s and (j == n or h[j] < h[s[-1]]):
                    m = s.pop()
                    width = j if not s else j - s[-1] - 1
                    answer = max(answer, h[m] * width)
                s.append(j)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        o = 6
        self.assertEqual(s.maximalRectangle(i), o)

    def test_two(self):
        s = Solution()
        i = [["0"]]
        o = 0
        self.assertEqual(s.maximalRectangle(i), o)

    def test_three(self):
        s = Solution()
        i = [["1"]]
        o = 1
        self.assertEqual(s.maximalRectangle(i), o)

    # def test_four(self):
    #     s = Solution()
    #     i = [["1"] * 200 for _ in range(200)]
    #     o = 200 * 200
    #     self.assertEqual(s.maximalRectangle(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)