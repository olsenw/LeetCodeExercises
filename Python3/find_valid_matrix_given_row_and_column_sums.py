# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two arrays rowSum and colSum of non-negative integers where rowSum[i]
    is the sum of the elements in the ith row and colSum[j] is the sum of the
    elements of the jth columns of a 2D matrix. In other words, the elements of
    the matrix are unknown, but the sums of each row and column are know.

    Find any matrix of non-negative integers of size
    rowSum.length x colSum.length that satisfies the rowSum and colSum
    requirements.

    Return a 2D array representing any matrix that fulfills the requirements. It
    is guaranteed that a least one matrix that fulfills the requirements exists.
    '''
    # based on leetcode solution
    # https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/submissions/1327964086/?envType=daily-question&envId=2024-07-20
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m,n = len(rowSum), len(colSum)
        currCol,currRow = [0]*n, [0]*m
        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                answer[i][j] = min(rowSum[i] - currRow[i], colSum[j] - currCol[j])
                currCol[j] += answer[i][j]
                currRow[i] += answer[i][j]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,8]
        j = [4,7]
        o = [[3,0],[1,7]]
        self.assertEqual(s.restoreMatrix(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,7,10]
        j = [8,6,8]
        o = [[0,5,0],
             [6,1,0],
             [2,0,8]]
        self.assertEqual(s.restoreMatrix(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)