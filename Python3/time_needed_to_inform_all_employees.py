# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A company has n employees with a unique ID for each employee from 0 to n-1.
    The head of the company is the one with headID.

    Each employee has one direct manager given in the manager array where
    manager[i] is the direct manager of the i-th employee, manager[headID] = -1.
    Also, it is guaranteed that the subordination relationships have a tree
    structure.

    The head of the company wants to inform all the company employees of an
    urgent piece of news. They will inform their direct subordinates, who will
    then inform their direct subordinates, and so on until all employees know
    about the urgent news.

    The i-th employee needs informTime[i] minutes to inform all of their direct
    subordinates (ie, after informTime[i] minutes, all their direct subordinates
    can start spreading the news).

    Return the number of minutes needed to inform all the employees about the
    urgent news.
    '''
    # incorrect events happen concurrently
    def numOfMinutes_incorrect(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {i:[] for i in range(n)}
        for i in range(n):
            if manager[i] == -1:
                continue
            graph[manager[i]].append(i)
        def dfs(i:int) -> int:
            return sum(dfs(j) for j in graph[i]) + informTime[i]
        return dfs(headID)
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {i:[] for i in range(n)}
        for i in range(n):
            if manager[i] == -1:
                continue
            graph[manager[i]].append(i)
        def dfs(i:int,j:int) -> int:
            if informTime[i] == 0:
                return j
            return max(dfs(k, j + informTime[i]) for k in graph[i])
        return dfs(headID,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        j = 0
        k = [-1]
        l = [0]
        o = 0
        self.assertEqual(s.numOfMinutes(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 6
        j = 2
        k = [2,2,-1,2,2,2]
        l = [0,0,1,0,0,0]
        o = 1
        self.assertEqual(s.numOfMinutes(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        i = 15
        j = 0
        k = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
        l = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
        o = 3
        self.assertEqual(s.numOfMinutes(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)