# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from itertools import accumulate
from bisect import bisect_left

class Solution:
    '''
    Given an integer array nums and an integer x. In one operation it is
    possible to remove the leftmost or the rightmost element from the
    array nums' and subtract its value from x. Note that this modifies
    the array for future operations.

    Return the minimum number of operations to reduce x to exactly 0 if
    it is possible otherwise, otherwise, return -1.
    '''
    # passes but very slow
    def minOperations_prefix_suffix(self, nums: List[int], x: int) -> int:
        n = len(nums)
        p = list(accumulate(nums))
        a, b = 0, 10**5 + 1
        i = bisect_left(p,x)
        if i < n and x == p[i]:
            b = min(b, i + 1)
        for i in range(n - 1, -1, -1):
            a += nums[i]
            if a == x:
                b = min(b, n - i)
            j = bisect_left(p,x - a,0,i)
            if j < i < n and a + p[j] == x:
                b = min(b, n - i + j + 1)
        return b if b < 10**5 + 1 else -1

    # improvement to above using hash table instead of search
    def minOperations_prefix_suffix_improved(self, nums: List[int], x: int) -> int:
        p = {j:i for i,j in enumerate(accumulate(nums))}
        a = 0
        b = 10 ** 5 + 1
        n = len(nums)
        if x in p:
            b = min(b, p[x] + 1)
        for i in range(len(nums) - 1, -1, -1):
            a += nums[i]
            if a == x:
                b = min(b, n - i)
            elif x - a in p:
                if p[x - a] < i:
                    b = min(b, n - i + p[x - a] + 1)
        return b if b < 10**5 + 1 else -1

    # sliding window (window is subarray when from sum equal x)
    # inspired from other leetcode solutions (ie when finally understood hints)
    # https://leetcode.com/submissions/api/detail/1776/python3/1057/
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        if s < x:
            return -1
        if s == x:
            return len(nums)
        # target sum of subarray
        t = s - x
        # left side of window
        # sum of window (accumulator)
        # largest window size
        l = a = m = 0
        # iterate over right side of window
        for r in range(len(nums)):
            a += nums[r]
            # force window less than or equal to target
            # ie update the left side of the window
            while a > t:
                a -= nums[l]
                l += 1
            # possible answer
            if a == t:
                m = max(m, r - l + 1)
        # must have found a window otherwise impossible
        return len(nums) - m if m > 0 else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,4,2,3]
        j = 5
        o = 2
        self.assertEqual(s.minOperations(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,6,7,8,9]
        j = 4
        o = -1
        self.assertEqual(s.minOperations(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3,2,20,1,1,3]
        j = 10
        o = 5
        self.assertEqual(s.minOperations(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,1]
        j = 3
        o = -1
        self.assertEqual(s.minOperations(i,j), o)

    def test_five(self):
        s = Solution()
        i = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
        j = 134365
        o = 16
        self.assertEqual(s.minOperations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)