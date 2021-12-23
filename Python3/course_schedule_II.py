# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are a total of numCourses courses which need to be taken. The
    courses are labeled from 0 to numCourses-1. You are given an array
    prerequisites where prerequisites[i] = [ai, bi] indicates that
    course bi must be taken before course ai.

    Return the ordering of courses you should take to finish all
    courses. If there are many valid answers, return any of them. It it
    is impossible to finish all courses, return an empty array.
    '''
    # this is slow due to many interactions with graph dictionary
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create graph
        graph = {i : set() for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].add(b)
        # print(graph)

        # Kahn's algorithm
        l = []
        s = set([i for i in graph if not graph[i]])
        for i in s:
            graph.pop(i)
        while s:
            n = s.pop()
            l.append(n)
            for i in list(graph.keys()):
                graph[i].discard(n)
                if not graph[i]:
                    s.add(i)
                    graph.pop(i)
        if graph:
            # cycle must be present
            return []
        return l

    # smarter way to access based on leetcode discussions
    # making use of deque is faster than set operations
    # tracking incoming edges vs deleting from a graph
    def findOrder_faster(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create graph
        graph = {i : set() for i in range(numCourses)}
        incoming = {}
        for a, b in prerequisites:
            graph[a].add(b)
            incoming[b] = incoming.get(b, 0) + 1
        # print(graph)

        # Kahn's algorithm
        l = []
        from collections import deque
        s = deque([i for i in range(numCourses) if i not in incoming])
        while s:
            n = s.popleft()
            l.append(n)
            if n in graph:
                for i in graph[n]:
                    incoming[i] -= 1
                    if incoming[i] == 0:
                        s.append(i)
        if len(l) == numCourses:
            l.reverse()
            return l
        # not all nodes used... must be cycle
        return []

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        n = 2
        e = [[1,0]]
        o = [0,1]
        self.assertEqual(s.findOrder(n, e), o)
        self.assertEqual(s.findOrder_faster(n, e), o)

    def test_two(self):
        s = Solution()
        n = 1
        e = []
        o = [0]
        self.assertEqual(s.findOrder(n, e), o)
        self.assertEqual(s.findOrder_faster(n, e), o)

    def test_three(self):
        s = Solution()
        n = 4
        e = [[1,0],[2,0],[3,1],[3,2]]
        o1 = [0,2,1,3]
        o2 = [0,1,2,3]
        a = s.findOrder(n, e)
        self.assertTrue(a == o1 or a == o2)
        a = s.findOrder_faster(n, e)
        self.assertTrue(a == o1 or a == o2)

if __name__ == '__main__':
    unittest.main(verbosity=2)