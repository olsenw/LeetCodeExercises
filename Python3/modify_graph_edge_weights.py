# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an undirected weighted connected graph containing n nodes labeled from
    0 to n-1, and an integer array edges where edges[i] = [ai, bi, wi] indicates
    that there is an edge between nodes ai and bi with weight wi.

    Some edges have a weight of -1 (wi = -1), while others have a positive wight
    (wi > 0).

    Modify all edges with a weight of -1 by assigning them positive integer
    values in the range[1, 2 * 10^9] so that the shortest distance between the
    nodes source and destination becomes equal to an integer target. If there
    are multiple modifications that make the shortest distance between source
    destination equal to target, any of them will be considered correct.

    Return an array containing all edges (even unmodified ones) in any order if
    it is possible to make the shortest distance from sources to destination
    equal to target, or an empty array if it's impossible.

    Note: it is impossible to modify the weights of edges with initial positive
    weights.
    '''
    def modifiedGraphEdges_incomplete(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = {i:dict() for i in range(n)}
        for i,j,k in edges:
            graph[i][j] = k
            graph[j][i] = k
        path = []
        def dijkstra(value:int) -> int:
            nonlocal path
            heap = [(0,source,[])]
            visited = set()
            while heap:
                x,y,z = heapq.heappop(heap)
                if y == destination:
                    path = list(z)
                    return x
                if y in visited:
                    continue
                visited.add(x)
                z = z + [y]
                for i in graph[y]:
                    if graph[y][i] > 0:
                        heapq.heappush(heap, (y + graph[y][i], i, z))
                    elif value > 0:
                        heapq.heappush(heap, (y + value, i, z))
            path = []
            return 0
        # hint 1: impossible if shortest path without edges is less than target
        # hint 2: impossible if shortest path with edges equal one is greater than target
        if dijkstra(0) < target or dijkstra(1) > target:
            return []
        return path

    # based on Leetcode editorial
    # https://leetcode.com/problems/modify-graph-edge-weights/editorial/?envType=daily-question&envId=2024-08-30
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        m = 10**9+7
        graph = [[] for _ in range(n)]
        # modified dijkstra using min heap and minimum distance table
        def dijkstra():
            distance = [m] * n
            distance[source] = 0
            heap = [(0,source)]
            while heap:
                x,y = heapq.heappop(heap)
                if x > distance[y]:
                    continue
                for i,j in graph[y]:
                    if x + j < distance[i]:
                        distance[i] = x + j
                        heapq.heappush(heap, (distance[i], i))
            return distance[destination]
        # build graph omitting -1 weight edges
        for x,y,z in edges:
            if z != -1:
                graph[x].append((y,z))
                graph[y].append((x,z))
        # find current shortest distance
        current = dijkstra()
        # hint 1: if shortest distance is less than target it is impossible
        # note that dijkstra case of unreachable returns very large value
        if current < target:
            return []
        # update edges if shortest path already equals target
        if current == target:
            for i in range(len(edges)):
                if edges[i][2] == -1:
                    edges[i][2] = m
            return edges
        # iterate over unknown weights
        for i, (x,y,z) in enumerate(edges):
            if z != -1:
                continue
            # try setting the weight to one
            edges[i][2] = 1
            graph[x].append((y,1))
            graph[y].append((x,1))
            # computer updated shortest distance
            current = dijkstra()
            # if less than or meeting target update edges
            if current <= target:
                edges[i][2] += target - current
                # set other edges to impossible value
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = m
                return edges
        # base case
        return []

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5
        o = [[4,1,1],[2,0,1],[0,3,1],[4,3,3]]
        self.assertEqual(s.modifiedGraphEdges(*i), o)

    def test_two(self):
        s = Solution()
        i = 3, [[0,1,-1],[0,2,5]], 0, 2, 6
        o = []
        self.assertEqual(s.modifiedGraphEdges(*i), o)

    def test_three(self):
        s = Solution()
        i = 4, [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], 0, 2, 6
        o = [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
        self.assertEqual(s.modifiedGraphEdges(*i), o)

    def test_four(self):
        s = Solution()
        i = 4, [[0,1,5],[1,2,7],[2,3,7],[3,1,9],[3,0,-1],[0,2,-1]], 2, 3, 7
        o = [[0,1,5],[1,2,7],[2,3,7],[3,1,9],[3,0,1000000007],[0,2,1000000007]]
        self.assertEqual(s.modifiedGraphEdges(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)