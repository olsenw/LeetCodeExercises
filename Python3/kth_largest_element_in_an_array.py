# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq

class Solution:
    '''
    Given an integer array nums and an integer k, return the kth largest
    element in the array.

    Note that it is the kth largest element in the sorted order, not the
    kth distinct element.
    '''
    def findKthLargest_sorted(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

    def findKthLargest_heapq(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        # for i in range(k, len(nums)):
        for n in nums[k:]:
            heapq.heappushpop(h, n)
        return h[0]

    def findKthLargest_heapq_nlargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    '''
    Could implement sort algorithm myself, or quick select, or divide
    and conquer... lots of options to solve this one.

    I went with sorted() and heapq because those are straight forward
    and conveniently built in.
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,1,5,6,4]
        j = 2
        o = 5
        self.assertEqual(s.findKthLargest_sorted(i, j), o)
        self.assertEqual(s.findKthLargest_heapq(i, j), o)
        self.assertEqual(s.findKthLargest_heapq_nlargest(i, j), o)

    def test_two(self):
        s = Solution()
        i = [3,2,3,1,2,4,5,5,6]
        j = 4
        o = 4
        self.assertEqual(s.findKthLargest_sorted(i,j), o)
        self.assertEqual(s.findKthLargest_heapq(i,j), o)
        self.assertEqual(s.findKthLargest_heapq_nlargest(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)