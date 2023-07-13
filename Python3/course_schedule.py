# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are a total of numCourses that have to be taken, labeled from 0 to
    numCourses - 1. Given an array prerequisites where 
    prerequisites[i] = [ai,bi] indicates that course bi must be taken before 
    course ai.

    Return true if it is possible to finish all courses. Otherwise, return
    false.
    '''
    # geeks for geeks on topological sort
    # https://www.geeksforgeeks.org/topological-sorting/
    # https://www.geeksforgeeks.org/detect-cycle-in-directed-graph-using-topological-sort/
    # if find cycle, it is impossible
    # (51/52 test cases) something is wrong... just not sure what
    def canFinish_invalid(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[a].append(b)
        stack = []
        visited = set()
        def topological(node):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    topological(i)
            stack.append(node)
        for i in range(numCourses):
            if i not in visited:
                topological(i)
        index = dict()
        for i in range(numCourses):
            index[stack[numCourses-1-i]] = i
        for i in range(numCourses):
            f = 0 if i not in index else index[i]
            for j in graph[i]:
                s = 0 if j not in index else index[j]
                if f > s:
                    # cycle detected
                    return False
        return True

    # based on leetcode dfs solution
    # https://leetcode.com/problems/course-schedule/editorial/
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[b].append(a)
        # visited nodes
        visit = [False] * numCourses
        # nodes in current dfs run
        stack = [False] * numCourses
        # return true if cycle detected
        def dfs(node):
            # cycle detected (current node is also an ancestor)
            if stack[node] == True:
                return True
            # already validated as not being part in cycle
            if visit[node] == True:
                return False
            visit[node] = True
            stack[node] = True
            for i in graph[node]:
                if dfs(i) == True:
                    return True
            stack[node] = False
            return False
        for i in range(numCourses):
            if dfs(i) == True:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = [[1,0]]
        o = True
        self.assertEqual(s.canFinish(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [[1,0],[0,1]]
        o = False
        self.assertEqual(s.canFinish(i,j), o)

    def test_three(self):
        s = Solution()
        i = 20
        j = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
        o = False
        self.assertEqual(s.canFinish(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)