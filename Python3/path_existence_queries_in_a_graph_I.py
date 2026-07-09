# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n representing the number of nodes in a graph, labeled from
    0 to n - 1.

    Also given an integer array nums of length n sorted in non-decreasing order,
    and an integer maxDiff.

    An undirected edge exists between nodes i and j if the absolute difference
    between nums[i] and nums[j] is at most maxDiff
    (ie |nums[i] - nums[j]| <= maxDiff).

    Given a 2D integer array queries. For each queries[i] = [ui, vi], determine
    whether there exists a path between nodes ui and vi.

    Return a boolean array answer, where answer[i] is true if there exists a
    path between ui and vi in the ith query and false otherwise.
    '''
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        groups = [0] * n
        g = 0
        upper = nums[0]
        for i,j in enumerate(nums):
            if j > upper:
                g += 1
            upper = j + maxDiff
            groups[i] = g                
        return [groups[i] == groups[j] for i,j in queries]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = [1,3]
        k = 1
        l = [[0,0],[0,1]]
        o = [True,False]
        self.assertEqual(s.pathExistenceQueries(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [2,5,6,8]
        k = 2
        l = [[0,1],[0,2],[1,3],[2,3]]
        o = [False,False,True,True]
        self.assertEqual(s.pathExistenceQueries(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)