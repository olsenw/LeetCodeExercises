# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, find three numbers whose product is maximum and
    return the maximum product.
    '''
    # does not account for negative numbers
    def maximumProduct_fails(self, nums: List[int]) -> int:
        h = []
        for n in nums:
            if len(h) < 3:
                heapq.heappush(h, n)
            else:
                heapq.heappushpop(h, n)
        return (h[0]) * (h[1]) * (h[2])

    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = 6
        self.assertEqual(s.maximumProduct(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        o = 24
        self.assertEqual(s.maximumProduct(i), o)

    def test_three(self):
        s = Solution()
        i = [-1,-2,-3]
        o = -6
        self.assertEqual(s.maximumProduct(i), o)

    def test_four(self):
        s = Solution()
        i = [-1000,-1000,1,2,3]
        o = 3000000
        self.assertEqual(s.maximumProduct(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)