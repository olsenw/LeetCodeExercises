# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict, deque
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a city that consists of n intersections numbered from 0 to n-1 with
    bi-directional roads between some intersections. The inputs are generated
    such that any intersection can be reached from any other intersection and
    there is at most one road between any two intersections.

    Given an integer n and a 2D integer array roads where
    roads[i] = [ui, vi, timei] means that there is a road between intersections
    ui and vi that takes timei minutes to travel. The number of ways to travel
    from intersection 0 to n-1 in the shortest amount of time is unknown.

    Return the number of ways to arrive at the destination in the shortest
    amount of time. Since the answer may be large, return it modulo 10**9 + 7.
    '''
    # wrong answer (does not account for recounted nodes)
    def countPaths_wrong(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for i,j,k in roads:
            graph[i][j] = k
            graph[j][i] = k
        heap = [(0,0)]
        visited = set()
        time = None
        answer = 0
        while heap:
            x,y = heapq.heappop(heap)
            if x == n - 1:
                if time is None:
                    time = y
                    answer = 1
                elif y == time:
                    answer += 1
                else:
                    return answer % (10**9 + 7)
            if x in visited:
                continue
            visited.add(x)
            for i in graph[x]:
                if i not in visited:
                    heapq.heappush(heap, (i, y + graph[x][i]))
        return answer

    def countPaths_tle(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for i,j,k in roads:
            graph[i][j] = k
            graph[j][i] = k
        heap = [(0,0)]
        visited = set()
        limit = 0
        while heap:
            y,x = heapq.heappop(heap)
            if x == n-1:
                limit = y
                break
            if x in visited:
                continue
            visited.add(x)
            for i in graph[x]:
                heapq.heappush(heap, (y + graph[x][i], i))
        visited = set()
        def dfs(node, depth):
            if node in visited or depth > limit:
                return 0
            if node == n - 1:
                return 1
            visited.add(node)
            s = sum(dfs(i, depth + graph[node][i]) for i in graph[node])
            visited.remove(node)
            return s
        pass
        return dfs(0,0) % (10**9 + 7)

    # based on solution by sagarsaini_
    # https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/solutions/5668196/simple-python-solution-beats-93-dijkstra-algo/
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for i,j,k in roads:
            graph[i][j] = k
            graph[j][i] = k
        ways = [0] * n
        ways[0] = 1
        distance = [float('inf')] * n
        distance[0] = 0
        heap = [(0,0)]
        while heap:
            y, x = heapq.heappop(heap)
            for i in graph[x]:
                time = y + graph[x][i]
                if time == distance[i]:
                    ways[i] += ways[x]
                elif time < distance[i]:
                    distance[i] = time
                    heapq.heappush(heap, (time, i))
                    ways[i] = ways[x]
        return ways[n-1] % (10**9 + 7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2, [[1,0,10]]
        o = 1
        self.assertEqual(s.countPaths(*i), o)

    def test_two(self):
        s = Solution()
        i = 7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
        o = 4
        self.assertEqual(s.countPaths(*i), o)

    def test_three(self):
        s = Solution()
        i = 18, [[0,1,3972],[2,1,1762],[3,1,4374],[0,3,8346],[3,2,2612],[4,0,6786],[5,4,1420],[2,6,7459],[1,6,9221],[6,3,4847],[5,6,4987],[7,0,14609],[7,1,10637],[2,7,8875],[7,6,1416],[7,5,6403],[7,3,6263],[4,7,7823],[5,8,10184],[8,1,14418],[8,4,11604],[7,8,3781],[8,2,12656],[8,0,18390],[5,9,15094],[7,9,8691],[9,6,10107],[9,1,19328],[9,4,16514],[9,2,17566],[9,0,23300],[8,9,4910],[9,3,14954],[4,10,26060],[2,10,27112],[10,1,28874],[8,10,14456],[3,10,24500],[5,10,24640],[10,6,19653],[10,0,32846],[10,9,9546],[10,7,18237],[11,7,21726],[11,2,30601],[4,11,29549],[11,0,36335],[10,11,3489],[6,11,23142],[3,11,27989],[11,1,32363],[11,8,17945],[9,11,13035],[5,11,28129],[2,12,33902],[5,12,31430],[6,12,26443],[4,12,32850],[12,3,31290],[11,12,3301],[12,1,35664],[7,13,28087],[13,8,24306],[6,13,29503],[11,13,6361],[4,13,35910],[13,12,3060],[3,13,34350],[13,5,34490],[13,2,36962],[10,13,9850],[9,13,19396],[12,14,8882],[8,14,30128],[14,6,35325],[14,5,40312],[1,14,44546],[11,14,12183],[15,12,13581],[2,15,47483],[4,15,46431],[15,10,20371],[15,14,4699],[15,6,40024],[15,7,38608],[1,15,49245],[11,15,16882],[8,15,34827],[0,15,53217],[5,15,45011],[15,3,44871],[16,2,53419],[16,9,35853],[1,16,55181],[16,7,44544],[8,16,40763],[0,16,59153],[15,16,5936],[16,10,26307],[16,6,45960],[12,16,19517],[17,2,57606],[17,3,54994],[17,14,14822],[17,11,27005],[0,17,63340],[17,7,48731],[8,17,44950],[17,16,4187],[5,17,55134],[17,10,30494],[17,9,40040],[17,12,23704],[13,17,20644],[17,1,59368]]
        o = 2891
        self.assertEqual(s.countPaths(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)