# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from itertools import accumulate
import bisect

class Solution:
    '''
    Given an m x n matrix matrix and an integer k, return the max sum of
    a rectangle in the matrix such that its sum is no larger than k.

    It is guaranteed that there will be a rectangle with a sum no larger
    than k.
    '''
    def maxSumSubmatrix_TimeLimitExceeded(self, matrix: List[List[int]], k: int) -> int:
        answer = -100
        m,n = len(matrix), len(matrix[0])
        prefix = [list(accumulate(i)) for i in matrix]
        for j in range(n):
            last = 0
            for i in range(m):
                prefix[i][j] = last = prefix[i][j] + last
        def sum(a,b,c,d):
            x = 0 if a == 0 or b == 0 else prefix[a-1][b-1]
            y = 0 if a == 0 else prefix[a-1][d]
            z = 0 if b == 0 else prefix[c][b-1]
            return prefix[c][d] + x - y - z
        for i in range(m):
            for j in range(n):
                for a in range(i+1):
                    for b in range(j+1):
                        s = sum(a,b,i,j)
                        if s <= k:
                            answer = max(answer,s)
        return answer

    # based off of discussion post by otoc
    # https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/445540/Python-bisect-solution-(960ms-beat-71.25)
    # reduces the problem to a smaller case... not sure why it works
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m,n = len(matrix), len(matrix[0])
        def maxSum1D(a):
            best = -1000000
            curr = 0
            ps = [1000000]
            for i in a:
                bisect.insort(ps, curr)
                curr += i
                j = bisect.bisect_left(ps, curr - k)
                best = max(best, curr - ps[j])
            return best
        rows = [list(accumulate(i)) for i in matrix]
        answer = -1000000
        for i in range(n):
            for j in range(i,n):
                a = [rows[k][j] - (rows[k][i-1] if i > 0 else 0) for k in range(m)]
                answer = max(answer, maxSum1D(a))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0,1],[0,-2,3]]
        j = 2
        o = 2
        self.assertEqual(s.maxSumSubmatrix(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[2,2,-1]]
        j = 3
        o = 3
        self.assertEqual(s.maxSumSubmatrix(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[1] * 100 for _ in range(100)]
        j = 50
        o = 50
        self.assertEqual(s.maxSumSubmatrix(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)