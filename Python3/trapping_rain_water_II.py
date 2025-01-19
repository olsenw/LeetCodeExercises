# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
from functools import cache
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n integer matrix heightMap representing the height of each unit
    cell in a 2D elevation map, return the volume of water it can trap after
    raining.
    '''
    def trapRainWater_fails(self, heightMap: List[List[int]]) -> int:
        m,n = len(heightMap), len(heightMap[0])
        visited = set()
        # @cache
        def dfs(x,y,h):
            if x < 0 or x == m or y < 0 or y == n:
                return 1
            if heightMap[x][y] >= h:
                return 1
            visited.add((x,y))
            a = 0
            if (x-1,y) not in visited:
                a += dfs(x-1,y,h)
            if (x-1,y) not in visited:
                a += dfs(x+1,y,h)
            if (x-1,y) not in visited:
                a += dfs(x,y-1,h)
            if (x-1,y) not in visited:
                a += dfs(x,y+1,h)
            visited.remove((x,y))
            return 1 if a else 0
        maxHeight = max(max(h) for h in heightMap)
        answer = 0
        for h in range(1,maxHeight):
            answer += m * n
            visited = set()
            for i in range(m):
                for j in range(n):
                    answer -= dfs(i,j,h)
        return answer

    # takes too long to perform bfs at every position height times
    def trapRainWater_tle(self, heightMap: List[List[int]]) -> int:
        m,n = len(heightMap), len(heightMap[0])
        maxHeight = max(max(h) for h in heightMap)
        def bfs(x,y,h):
            visited = set()
            queue = deque([(x,y)])
            while queue:
                i,j = queue.popleft()
                if i < 0 or i == m or j < 0 or j == n:
                    return False
                visited.add((i,j))
                if heightMap[i][j] >= h:
                    continue
                if (i-1,j) not in visited:
                    queue.append((i-1,j))
                if (i+1,j) not in visited:
                    queue.append((i+1,j))
                if (i,j-1) not in visited:
                    queue.append((i,j-1))
                if (i,j+1) not in visited:
                    queue.append((i,j+1))
            return True
        answer = 0
        for h in range(1,maxHeight+1):
            for i in range(m):
                for j in range(n):
                    if heightMap[i][j] < h and bfs(i,j,h):
                        answer += 1
        return answer

    # based on leetcode editorial
    # https://leetcode.com/problems/trapping-rain-water-ii/?envType=daily-question&envId=2025-01-19
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m,n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        for i in range(m):
            heapq.heappush(heap, [heightMap[i][0],i,0])
            visited[i][0] = True
            heapq.heappush(heap, [heightMap[i][n-1],i,n-1])
            visited[i][n-1] = True
        for j in range(1,n-1):
            heapq.heappush(heap, [heightMap[0][j],0,j])
            visited[0][j] = True
            heapq.heappush(heap, [heightMap[m-1][j],m-1,j])
            visited[m-1][j] = True
        answer = 0
        while heap:
            height,i,j = heapq.heappop(heap)
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if heightMap[x][y] < height:
                        answer += height - heightMap[x][y]
                    heapq.heappush(heap, [max(height,heightMap[x][y]),x,y])
                    visited[x][y] = True
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
        o = 4
        self.assertEqual(s.trapRainWater(i), o)

    def test_two(self):
        s = Solution()
        i = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
        o = 10
        self.assertEqual(s.trapRainWater(i), o)

    def test_three(self):
        s = Solution()
        i = [[2,2,2],[2,0,2],[2,2,2]]
        o = 2
        self.assertEqual(s.trapRainWater(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)