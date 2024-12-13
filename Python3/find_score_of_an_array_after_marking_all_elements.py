# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums consisting of positive integers.

    Starting with score = 0, apply the following algorithm:
    * Choose te smallest integer of the array that is not marked. If there is a
      tie, choose the one with the smallest index.
    * Add the value of the chosen integer to score.
    * Mark the chosen element and its two adjacent elements if they exist.
    * Repeat until all the array elements are marked.

    Return the score after applying the above algorithm.
    '''
    # fails heapq.heapify does not allow lambda key
    def findScore_runtime_error(self, nums: List[int]) -> int:
        score = 0
        indices = list(range(len(nums)))
        heapq.heapify(indices, key=lambda i: (indices[i], i))
        marked = set()
        while indices:
            i = heapq.heappop(indices)
            if i in marked:
                continue
            marked.add(i-1)
            marked.add(i)
            marked.add(i+1)
            score += indices[i]
        return score

    def findScore(self, nums: List[int]) -> int:
        score = 0
        marked = set()
        for j,i in sorted((j,i) for i,j in enumerate(nums)):
            if i in marked:
                continue
            marked.add(i-1)
            marked.add(i)
            marked.add(i+1)
            score += j
        return score

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,3,4,5,2]
        o = 7
        self.assertEqual(s.findScore(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,5,1,3,2]
        o = 5
        self.assertEqual(s.findScore(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)