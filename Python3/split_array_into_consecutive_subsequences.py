# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq

class Solution:
    '''
    Given an integer array nums that is sorted in non-decreasing order.

    Determine if it is possible to split nums into one or more
    subsequences such that both of the following conditions are true:
    * Each subsequence is a consecutive increasing sequence (i.e. each 
      integer is exactly one more than the previous integer).
    * All subsequences have a length of 3 or more.

    Return true if is possible to split nums according to the above
    conditions, or false otherwise.

    A subsequence of an array is a new array that is formed from the
    original array by deleting some (can be none) of the elements
    without disturbing the relative positions of the remaining element.
    '''
    def isPossible_passes(self, nums: List[int]) -> bool:
        h = []
        for n in nums:
            valid = []
            while h:
                l,v = h[0]
                if v == n - 1:
                    heapq.heapreplace(h, (l+1, n))
                    break
                elif v == n:
                    valid.append(heapq.heappop(h))
                else:
                    if heapq.heappop(h)[0] < 3:
                        return False
            else:
                heapq.heappush(h, (1,n))
            for v in valid:
                if v[0] < 3 and v[1] < n:
                    return False
                heapq.heappush(h,v)
        return not any(i < 3 for i,_ in h)

    '''
    try an alternate solution using two counters, one that is what I
    have, and the other is what I need.
    See sample 746ms submission for full idea.
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,3,4,5]
        o = True
        self.assertEqual(s.isPossible(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,3,4,4,5,5]
        o = True
        self.assertEqual(s.isPossible(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,4,5]
        o = False
        self.assertEqual(s.isPossible(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)