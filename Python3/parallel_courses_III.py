# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, which indicates that there are n courses labeled from 1
    to n. Also given a 2D integer array relations where 
    relations[j] = [prevCoursej, nextCoursej] denotes that course prevCoursej
    has to be completed before course nextCoursej (prerequisite relationship).
    Furthermore, also given is a 0-indexed integer array time where time[i]
    denotes how many months it takes to complete the (i+1)th course.

    Find the minimum number of months needed to complete all the courses
    following these rules:
    * A course may be started at any time as long as prerequisites are met.
    * Any number of courses can be taken at the same time.

    Return the minimum number of months needed to complete all the courses.

    Note: The test cases are generated such that it is possible to complete
    every course (ie, the graph is a directed acyclic graph).
    '''
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = {i:[0,[]] for i in range(n)}
        for i,j in relations:
            graph[j-1][0] += 1
            graph[i-1][1].append(j-1)
        @cache
        def dfs(root):
            return max((dfs(i) for i in graph[root][1]), default=0) + time[root]
            # a = max((dfs(i) for i in graph[root][1]), default=0)
            # return a + time[root]
        return max(dfs(i) for i in graph if graph[i][0] == 0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[1,3],[2,3]]
        k = [3,2,5]
        o = 8
        self.assertEqual(s.minimumTime(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [[1,5],[2,5],[3,5],[3,4],[4,5]]
        k = [1,2,3,4,5]
        o = 12
        self.assertEqual(s.minimumTime(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)