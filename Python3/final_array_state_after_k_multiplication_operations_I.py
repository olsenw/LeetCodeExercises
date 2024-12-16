# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, an integer k, and an integer multiplier.

    Perform k operations on nums. In each operation:
    * Find the minimum value x in nums. If there are multiple occurrences of the
      minimum value, select the one that appears first.
    * Replace the selected minimum value x with x * multiplier.

    Return an integer array denoting the final state of nums after performing
    all k operations. 
    '''
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(j,i) for i,j in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            x,y = heap[0]
            heapq.heapreplace(heap, (x * multiplier, y))
        for x,y in heap:
            nums[y] = x
        return nums

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,3,5,6]
        j = 5
        k = 2
        o = [8,4,6,5,6]
        self.assertEqual(s.getFinalState(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        j = 3
        k = 4
        o = [16,8]
        self.assertEqual(s.getFinalState(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)