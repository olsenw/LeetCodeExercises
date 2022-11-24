# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import deque,Counter

class Solution:
    def exist_dfs_bfs_fails(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        def bfs(x,y,w):
            queue = deque([(x,y,w)])
            visited = set()
            while queue:
                a,b,c = queue.popleft()
                if (a,b) in visited or not word.startswith(c):
                    continue
                if c == word:
                    return True
                visited.add((a,b))
                if a > 0:
                    queue.append((a-1,b,c+board[a-1][b]))
                if a < m - 1:
                    queue.append((a+1,b,c+board[a+1][b]))
                if b > 0:
                    queue.append((a,b-1,c+board[a][b-1]))
                if b < n - 1:
                    queue.append((a,b+1,c+board[a][b+1]))
            return False
        visited = set()
        def dfs(x,y,w):
            if (x,y) in visited:
                return False
            visited.add((x,y))
            if word.startswith(w):
                if w == word:
                    return True
                if x > 0 and dfs(x-1,y,w+board[x-1][y]):
                    return True
                if x < m -1 and dfs(x+1,y,w+board[x+1][y]):
                    return True
                if y > 0 and dfs(x,y-1,w+board[x][y-1]):
                    return True
                if y < n - 1 and dfs(x,y+1,w+board[x][y+1]):
                    return True
            visited.remove((x,y))
            return False
        for i in range(m):
            for j in range(n):
                # if board[i][j] == word[0] and bfs(i,j,word[0]):
                if board[i][j] == word[0] and dfs(i,j,word[0]):
                    return True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        def possible():
            a = Counter(word.upper())
            b = Counter()
            for row in board:
                for c in row:
                    b[c.upper()] += 1
            return all(a[c] <= b[c] for c in a) 
        visited = set()
        def dfs(x,y,w):
            if len(w) == 1 and board[x][y] == w:
                return True
            if board[x][y] != w[0]:
                return False
            visited.add((x,y))
            if x > 0 and (x-1,y) not in visited and dfs(x-1,y,w[1:]): return True
            if x < m - 1 and (x+1,y) not in visited and dfs(x+1,y,w[1:]): return True
            if y > 0 and (x,y-1) not in visited and dfs(x,y-1,w[1:]): return True
            if y < n - 1 and (x,y+1) not in visited and dfs(x,y+1,w[1:]): return True
            visited.remove((x,y))
            return False
        return possible() and any(dfs(x,y,word) for x in range(m) for y in range(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        j = "ABCCED"
        o = True
        self.assertEqual(s.exist(i,j), o)

    def test_two(self):
        s = Solution()
        i = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        j = "SEE"
        o = True
        self.assertEqual(s.exist(i,j), o)

    def test_three(self):
        s = Solution()
        i = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        j = "ABCB"
        o = False
        self.assertEqual(s.exist(i,j), o)

    def test_Four(self):
        s = Solution()
        i = [["A"]]
        j = "A"
        o = True
        self.assertEqual(s.exist(i,j), o)

    def test_Five(self):
        s = Solution()
        i = [["A"]]
        j = "B"
        o = False
        self.assertEqual(s.exist(i,j), o)

    def test_Six(self):
        s = Solution()
        i = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
        j = "ABCESEEEFS"
        o = True
        self.assertEqual(s.exist(i,j), o)

    def test_Six(self):
        s = Solution()
        i = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
        j = "AAAAAAAAAAAABAA"
        o = False
        self.assertEqual(s.exist(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)