# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n cities numbered from 0 to n-1. Given the array edges where
    edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted
    edge between cities fromi and toi and given the integer distanceThreshold.

    Return the city with the smallest number of cities that are reachable
    through some path and whose distance is at most distanceThreshold, if there
    are multiple such cities, return the city with the greatest number.

    Notice that the distance of a path connecting cities i and j is equal to the
    sum of the edges' weights along that path.
    '''
    # has some logic issue
    def findTheCity_wrong(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[0] * n for _ in range(n)]
        for i,j,k in edges:
            graph[i][j] = k
            graph[j][i] = k
        visited = set()
        def dfs(node, distance):
            answer = 0
            visited.add(node)
            for i in range(n):
                if i not in visited and i != node and 0 < graph[node][i] <= distance:
                    answer += 1 + dfs(i, distance - graph[node][i])
            visited.remove(node)
            return answer
        answer = [(dfs(i, distanceThreshold), -i) for i in range(n)]
        return -min(answer)[1]

    def findTheCity_wrong(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[0] * n for _ in range(n)]
        for i,j,k in edges:
            graph[i][j] = k
            graph[j][i] = k
        def bfs(node):
            h = [(node,distanceThreshold)]
            v = set()
            while h:
                x,y = heapq.heappop(h)
                v.add(x)
                for i in range(n):
                    if i not in v and 0 < graph[x][i] <= y:
                        heapq.heappush(h, (i, y - graph[x][i]))
            return len(v) - 1
        return min((i for i in range(n-1, -1, -1)), key=lambda x: bfs(x))

    def findTheCity_wrong(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = {i:defaultdict(int) for i in range(n)}
        for i,j,k in edges:
            graph[i][j] = k
            graph[j][i] = k
        def bfs(node):
            h = [(distanceThreshold, node)]
            v = set()
            while h:
                y,x = heapq.heappop(h)
                v.add(x)
                for i in graph[x]:
                    if i not in v and 0 < graph[x][i] <= y:
                        heapq.heappush(h, (y - graph[x][i], i))
            return len(v) - 1
        return min((i for i in range(n-1,-1,-1)), key=lambda x: (bfs(x),-x))

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = {i:defaultdict(int) for i in range(n)}
        for i,j,k in edges:
            graph[i][j] = k
            graph[j][i] = k
        def bfs(node):
            h = [(0, node)]
            visited = set()
            while h:
                distance, current = heapq.heappop(h)
                if distance > distanceThreshold:
                    continue
                visited.add(current)
                for i in graph[current]:
                    if i not in visited:
                        heapq.heappush(h, (distance + graph[current][i], i))
            return len(visited) - 1
        return min((i for i in range(n-1,-1,-1)), key=lambda x: bfs(x))

    '''
    See Leetcode editorial for smarter solutions

    Based around Dijkstra or Floyd-Warshall's algorithm
    '''
class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
        k = 4
        o = 3
        self.assertEqual(s.findTheCity(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
        k = 2
        o = 0
        self.assertEqual(s.findTheCity(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 6
        j = [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]]
        k = 5
        o = 5
        self.assertEqual(s.findTheCity(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 6
        j = [[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]]
        k = 417
        o = 5
        self.assertEqual(s.findTheCity(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)