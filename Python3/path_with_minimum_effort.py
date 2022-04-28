# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution: 
    '''
    A hiker is preparing for an upcoming hike. Given heights, a 2D array
    of size rows x columns, were heights[row][col] represents the height
    of cell (row, col). The hiker is situated in the top-left cell
    (0,0), and the hiker hopes to travel to the bottom-right cell
    (rows-1, columns-1) (0-indexed). The hiker can move up, down, left,
    or right and the hiker wants the route with the minimum effort.

    A route's effort is the maximum absolute difference in heights
    between two consecutive cells of the route.

    Return the minimum effort required to travel from the top-left cell
    to the bottom right cell.
    '''
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        if rows == cols == 1:
            return 0
        # src node -> [(edge weight, dst node), ...]
        graph = dict()
        for i in range(rows):
            for j in range(cols):
                p = i * cols + j
                graph[p] = []
                # edge right
                if j < cols - 1:
                    w = abs(heights[i][j] - heights[i][j+1])
                    graph[p].append((w, p + 1))
                # edge left
                if j > 0:
                    w = abs(heights[i][j] - heights[i][j-1])
                    graph[p].append((w, p - 1))
                # edge down
                if i < rows - 1:
                    w = abs(heights[i][j] - heights[i+1][j])
                    graph[p].append((w, p + cols))
                # edge up
                if i > 0:
                    w = abs(heights[i][j] - heights[i-1][j])
                    graph[p].append((w, p - cols))
        # does search using graph
        def search(threshold):
            target = rows * cols - 1
            visited = [False] * (rows * cols)
            nodes = [0]
            while nodes:
                update = []
                for n in nodes:
                    if n == target:
                        return True
                    if not visited[n]:
                        visited[n] = True
                        for i,j in graph[n]:
                            if i <= threshold and not visited[j]:
                                update.append(j)
                nodes = update
            return False
        # boundaries for binary search
        bot = 0
        top = max(max(graph[i], key=lambda x: x[0]) for i in graph)[0]
        while bot < top:
            mid = (bot + top) // 2
            if search(mid):
                top = mid
            else:
                bot = mid + 1
        return top

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,2],[3,8,2],[5,3,5]]
        o = 2
        self.assertEqual(s.minimumEffortPath(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3],[3,8,4],[5,3,5]]
        o = 1
        self.assertEqual(s.minimumEffortPath(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
        o = 0
        self.assertEqual(s.minimumEffortPath(i), o)

    def test_four(self):
        s = Solution()
        i = [[3]]
        o = 0
        self.assertEqual(s.minimumEffortPath(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)