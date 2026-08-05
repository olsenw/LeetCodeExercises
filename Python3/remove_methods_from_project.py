# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a project with n methods numbered from 0 to n-1.

    Given two integers n and k, and a 2D integer array invocations, where 
    invocations[i] = [ai, bi] indicates that method ai invokes method bi.

    There is a known bug in method k. Method k, along with any method invoked by
    it, either directly or indirectly, are considered suspicious and need to be
    removed.

    A group of methods can only be removed if no method outside the group
    invokes any methods within it.

    Return an array containing all te remaining methods after removing all the
    suspicious methods. The answer may be returned in any order. If it is not
    possible to remove all the suspicious methods, none should be removed.
    '''
    def remainingMethods_fails(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        marked = [False] * n
        graph = {i:[] for i in range(n)}
        for i,j in invocations:
            graph[i].append(j)
        def bfs(node:int, t:bool) -> None:
            queue = deque([node])
            while queue:
                a = queue.popleft()
                if marked[a] == t:
                    continue
                marked[a] = t
                for b in graph[a]:
                    if marked[b] != t:
                        queue.append(b)
        bfs(k, True)
        pass
        for i in range(n):
            if marked[i] == False:
                for j in graph[i]:
                    bfs(j, False)
        return [i for i in range(n) if marked[i] == False]

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        marked = [False] * n
        graph = {i:[] for i in range(n)}
        for i,j in invocations:
            graph[i].append(j)
        def bfs(node:int, t:bool) -> None:
            queue = deque([node])
            while queue:
                a = queue.popleft()
                if marked[a] == t:
                    continue
                marked[a] = t
                for b in graph[a]:
                    if marked[b] != t:
                        queue.append(b)
        bfs(k, True)
        visited = set()
        @cache
        def dfs(node:int) -> bool:
            if marked[node]:
                return True
            if node in visited:
                return False
            visited.add(node)
            return any(dfs(i) for i in graph[node])
        pass
        for i in range(n):
            visited.clear()
            if marked[i] == False and dfs(i):
                return list(range(n))
        return [i for i in range(n) if marked[i] == False]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = 1
        k = [[1,2],[0,1],[3,2]]
        o = [0,1,2,3]
        self.assertEqual(s.remainingMethods(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = 0
        k = [[1,2],[0,2],[0,1],[3,4]]
        o = [3,4]
        self.assertEqual(s.remainingMethods(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = 2
        k = [[1,2],[0,1],[2,0]]
        o = []
        self.assertEqual(s.remainingMethods(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 3
        j = 2
        k = [[1,0],[2,0]]
        o = [0,1,2]
        self.assertEqual(s.remainingMethods(i,j,k), o)

    def test_five(self):
        s = Solution()
        i = 3
        j = 0
        k = [[1,2],[2,1]]
        o = [1,2]
        self.assertEqual(s.remainingMethods(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)