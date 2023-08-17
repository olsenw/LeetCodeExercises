# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def updateMatrix_fails(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        v = set()
        @cache
        def bfs(i,j):
            if mat[i][j] == 0:
                return 0
            answer = m * n
            v.add((i,j))
            if i > 0 and (i-1,j) not in v:
                answer = min(answer, 1 + bfs(i-1,j))
            if i < m - 1 and (i+1,j) not in v:
                answer = min(answer, 1 + bfs(i+1,j))
            if j > 0 and (i,j-1) not in v:
                answer = min(answer, 1 + bfs(i,j-1))
            if j < n - 1 and (i,j+1) not in v:
                answer = min(answer, 1 + bfs(i,j+1))
            v.remove((i,j))
            return answer
        return [[bfs(i,j) for j in range(n)] for i in range(m)]

    def updateMatrix_tle(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        answer = [[m*n] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    answer[i][j] = 0
                    continue
                q = deque([(i,j,0)])
                s = set()
                while q:
                    x,y,z = q.popleft()
                    if (x,y) in s:
                        continue
                    s.add((x,y))
                    if mat[x][y] == 0:
                        answer[i][j] = min(z, answer[i][j])
                        break
                    # if mat[x][y] == 0:
                    #     answer[i][j] = min(z, answer[i][j])
                    #     # break
                    # if answer[x][y] != m * n:
                    #     answer[i][j] = min(z + answer[x][y], answer[i][j])
                    #     # break
                    if x > 0:
                        q.append((x-1,y,z+1))
                    if x < m - 1:
                        q.append((x+1,y,z+1))
                    if y > 0:
                        q.append((x,y-1,z+1))
                    if y < n - 1:
                        q.append((x,y+1,z+1))
        return answer

    # based on solution by shivaerrak
    # https://leetcode.com/problems/01-matrix/solutions/3920312/python-java-c-simple-solution/
    # oposite of what above, make the zeros spread (updated answers)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        answer = [[m*n] * n for _ in range(m)]
        # find all zeros
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    answer[i][j] = 0
                    q.append((i,j))
        # for each element in queue update if better path found
        while q:
            i,j = q.popleft()
            if i - 1 >= 0 and answer[i-1][j] > 1 + answer[i][j]:
                answer[i-1][j] = 1 + answer[i][j]
                q.append((i-1,j))
            if i + 1 < m and answer[i+1][j] > 1 + answer[i][j]:
                answer[i+1][j] = 1 + answer[i][j]
                q.append((i+1,j))
            if j - 1 >= 0 and answer[i][j-1] > 1 + answer[i][j]:
                answer[i][j-1] = 1 + answer[i][j]
                q.append((i,j-1))
            if j + 1 < n and answer[i][j+1] > 1 + answer[i][j]:
                answer[i][j+1] = 1 + answer[i][j]
                q.append((i,j+1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0,0],[0,1,0],[0,0,0]]
        o = [[0,0,0],[0,1,0],[0,0,0]]
        self.assertEqual(s.updateMatrix(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0,0],[0,1,0],[1,1,1]]
        o = [[0,0,0],[0,1,0],[1,2,1]]
        self.assertEqual(s.updateMatrix(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
        o = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
        self.assertEqual(s.updateMatrix(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)