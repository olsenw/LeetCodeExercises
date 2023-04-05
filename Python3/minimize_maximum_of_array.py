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
    Given a 0-indexed array nums comprising of n non-negative integers.

    In one operation:
    * Choose an integer i such that 1 <= i < n and nums[i] > 0.
    * Decrease nums[i] by 1.
    * Increase nums[i-1] by 1.

    Return the minimum possible value of the maximum integer of nums after
    performing any number of operations.
    '''
    # O(n^2)
    def minimizeArrayValue_queue(self, nums: List[int]) -> int:
        h = [nums[0]]
        for n in nums[1:]:
            while h[0] < n:
                n -= 1
                heapq.heapreplace(h, h[0] + 1)
            heapq.heappush(h,n)
        return max(h)

    def minimizeArrayValue_incorrect(self, nums: List[int]) -> int:
        m = nums[0]
        soak = 0
        for i,n in enumerate(nums[1:],2):
            if n > m:
                if n-m > soak:
                    a = n - m - soak
                    # somethings is wrong here
                    soak = n - m - a
                    m += a // i
                else:
                    soak -= n-m
            else:
                soak += m - n
        return m

    # based on solution by leetcode
    # https://leetcode.com/problems/minimize-maximum-of-array/editorial/
    # idea of soak was good, nonsense I was trying to do with it made no sense
    # here keep track of prefix and then find average (which is maximum) for
    # that part of array and return largest needed to solve
    def minimizeArrayValue(self, nums: List[int]) -> int:
        a = 0 # max value
        p = 0 # prefix sum
        for i,n in enumerate(nums,1):
            p += n
            # average (round up) of prefix / cells traversed
            b = math.ceil(p / i)
            # need the biggest of any iteration
            a = max(a,b)
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,7,1,6]
        o = 5
        self.assertEqual(s.minimizeArrayValue(i), o)

    def test_two(self):
        s = Solution()
        i = [10,1]
        o = 10
        self.assertEqual(s.minimizeArrayValue(i), o)

    def test_three(self):
        s = Solution()
        i = [1,10]
        o = 6
        self.assertEqual(s.minimizeArrayValue(i), o)

    def test_four(self):
        s = Solution()
        i = [1,2,3,4,5,6,7,8,9,0]
        o = 5
        self.assertEqual(s.minimizeArrayValue(i), o)

    def test_five(self):
        s = Solution()
        i = [1,3,6,1,1,1,2,9,1,22]
        o = 5
        self.assertEqual(s.minimizeArrayValue(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)