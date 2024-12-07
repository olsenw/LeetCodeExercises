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
    Given an integer array nums where the ith bag contains nums[i] balls. Also
    given an integer maxOperations.

    Perform the following operation at most maxOperations times:
    * Take any bag of balls and divide it into two new bags with a positive
      number of balls.
    
    Penalty is the maximum number of balls in a bag. Minimize the penalty after
    the operations.

    Return the minimum possible penalty after performing the operations.
    '''
    # do not always want to split into biggest halves
    # example 9 -> [5,4] is worse than 9 -> [6,3] for maxOperations = 3
    def minimumSize_fails(self, nums: List[int], maxOperations: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        for _ in range(maxOperations):
            n = heapq.heappop(heap)
            a,b = divmod(n, 2)
            b = a + b
            if a:
                heapq.heappush(heap, a)
            if b:
                heapq.heappush(heap, b)
        return -min(heap)

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        i,j = 1, max(nums)
        while i < j:
            k = i + (j - i) // 2
            count = 0
            for n in nums:
                if n > k:
                    a,b = divmod(n, k)
                    count += a if b else a - 1
            if count > maxOperations:
                i = k + 1
            else:
                j = k
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [9]
        j = 2
        o = 3
        self.assertEqual(s.minimumSize(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,4,8,2]
        j = 4
        o = 2
        self.assertEqual(s.minimumSize(i,j), o)

    def test_three(self):
        s = Solution()
        i = [9]
        j = 40
        o = 1
        self.assertEqual(s.minimumSize(i,j), o)

    def test_four(self):
        s = Solution()
        i = [9,200,500,2,2,80]
        j = 40
        o = 19
        self.assertEqual(s.minimumSize(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)