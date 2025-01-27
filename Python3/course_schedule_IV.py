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
    There are a total of numCourses courses to take, labeled from 0 to
    numCourses - 1. Given an array prerequisites where
    prerequisites[i] = [ai, bi] indicates that course ai must be taken before
    course bi.

    Prerequisites can also be indirect. If course a is a perquisite of course b,
    and course b is a prerequisite of course c, then course a is a prerequisite
    of course c.

    Also given an array queries where queries[j] = [uj, vj]. For the jth query,
    answer if course uj is a prerequisite of course vj or not.

    Return a boolean array answer, where answer[j] is the answer of the jth
    query.
    '''
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reverseGraph = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            reverseGraph[b].append(a)
        @cache
        def dfs(source, target):
            if source == target:
                return True
            for i in reverseGraph[source]:
                if dfs(i, target):
                    return True
            return False
        answer = []
        for a,b in queries:
            answer.append(dfs(b,a))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = [[1,0]]
        k = [[0,1],[1,0]]
        o = [False,True]
        self.assertEqual(s.checkIfPrerequisite(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = []
        k = [[0,1],[1,0]]
        o = [False,False]
        self.assertEqual(s.checkIfPrerequisite(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [[1,2],[1,0],[2,0]]
        k = [[1,0],[1,2]]
        o = [True,True]
        self.assertEqual(s.checkIfPrerequisite(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)