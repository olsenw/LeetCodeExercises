# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array gifts denoting the number of gifts in various piles.
    Every second the following occurs:
    * Choose the pile with the maximum number of gifts.
    * If there is more than one pile with the maximum number of gifts, choose
      any.
    * Leave behind the floor of the square root of the number of gifts in the
      pile. Take the rest of the gifts.
    
    Return the number of gifts remaining after k seconds.
    '''
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            leave = math.isqrt(-heap[0])
            heapq.heapreplace(heap, -leave)
        return -sum(heap)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [25,64,9,4,100]
        j = 4
        o = 29
        self.assertEqual(s.pickGifts(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1]
        j = 4
        o = 4
        self.assertEqual(s.pickGifts(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)