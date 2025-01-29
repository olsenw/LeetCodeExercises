# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict, deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    In this problem, a tree is an undirected graph hat is connected and has no
    cycles.

    Given a graph that started as a tree with n nodes labeled from 1 to n, with
    one additional edge added. The added edge has two different vertices chosen
    from 1 to n, and was not an edge that already existed. The graph is
    represented as an array edges of length n where edges[i] = [ai, bi]
    indicates that there is an edge between nodes ai and bi in the graph.

    Return an edge that can be removed so that the resulting graph is a tree of
    n nodes. If there are multiple answers, return the answer that occurs last
    in the input.
    '''
    def findRedundantConnection_fails(self, edges: List[List[int]]) -> List[int]:
        n = 0
        graph = defaultdict(list)
        for a,b in edges:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
            n = max(n, a, b)
        def bfs(e):
            visited = [False] * n
            last = -1
            queue = deque([0])
            while queue:
                i = queue.popleft()
                for j in graph[i]:
                    if j == last or [min(i,j),max(i,j)] == e:
                        continue
                    if visited[j]:
                        return False
                    visited[j] = True
                    queue.append(j)
                last = i
            return all(visited)
        for a,b in edges[::-1]:
            e = [min(a-1,b-1),max(a-1,b-1)]
            if bfs(e):
                return e
        return 

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(set)
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        def bfs(a,b):
            graph[a].remove(b)
            graph[b].remove(a)
            visited = dict()
            visited[1] = 0
            queue = deque([1])
            while queue:
                i = queue.popleft()
                for j in graph[i]:
                    # do not loop back to previous node
                    if j in visited and visited[i] == j:
                        continue
                    # cycle
                    if j in visited:
                        graph[a].add(b)
                        graph[b].add(a)
                        return False
                    visited[j] = i
                    queue.append(j)
            graph[a].add(b)
            graph[b].add(a)
            return len(visited) == n
        for a,b in edges[::-1]:
            if bfs(a,b):
                return [a,b]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[1,3],[2,3]]
        o = [2,3]
        self.assertEqual(s.findRedundantConnection(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        o = [1,4]
        self.assertEqual(s.findRedundantConnection(i), o)

    def test_three(self):
        s = Solution()
        i = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]
        o = [2,8]
        self.assertEqual(s.findRedundantConnection(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)