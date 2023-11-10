# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an integer array nums that consists of n unique elements, but it
    has been forgotten. However, every pair of adjacent elements is known.

    Given a 2D integer array adjacentPairs of size n - 1 where each
    adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are
    adjacent in nums.

    It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1]
    will exist in adjacentPairs, either as [nums[i], nums[i+1]] or
    [nums[i+1], nums[i]]. The pairs can appear in any order.

    Return the original array nums. If there are multiple solutions, return any
    of them.
    '''
    # based on leetcode solution
    # https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/editorial/?envType=daily-question&envId=2023-11-10
    # I was oversimplifying the problem.
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i,j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)
        root = 0
        for i in graph:
            if len(graph[i]) == 1:
                root = i
                break
        curr = root
        prev = None
        answer = [curr]
        while len(answer) < len(adjacentPairs) + 1:
            for i in graph[curr]:
                if i != prev:
                    answer.append(i)
                    prev = curr
                    curr = i
                    break
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,1],[3,4],[3,2]]
        o = [1,2,3,4]
        self.assertEqual(s.restoreArray(i), o)

    def test_two(self):
        s = Solution()
        i = [[4,-2],[1,4],[-3,1]]
        o = [-2,4,1,-3]
        self.assertEqual(s.restoreArray(i), o)

    def test_three(self):
        s = Solution()
        i = [[100000,-100000]]
        o = [100000,-100000]
        self.assertEqual(s.restoreArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)