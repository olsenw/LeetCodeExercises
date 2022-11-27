# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums, return the number of all the arithmetic
    subsequences of nums.

    A sequence of numbers is called arithmetic if it consists of at least three
    elements and if the difference between any two consecutive elements is the
    same.

    A subsequence of an array is sequence that can be formed by removing some
    elements (possibly none) of the array.

    The test cases are generated such that the answer fits in a 32-bit integer.
    '''
    def numberOfArithmeticSlices_incomplete(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i,j):
            c, d = 0, nums[j] - nums[i]
            for k in range(j+1,n):
                if nums[k] - nums[j] == d:
                    c += 1 + dp(j,k)
            return c 
        return sum(dp(0,i) for i in range(n))

    # based on leetcode dynamic programming solution
    # https://leetcode.com/problems/arithmetic-slices-ii-subsequence/solution/
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # keeps track of weak subsequences (ie length 2)
        cnt = [None] * n
        for i in range(n):
            # map indices to differences
            cnt[i] = defaultdict(int)
            for j in range(i):
                d = nums[j] - nums[i]
                s = cnt[j][d]
                o = cnt[i][d]
                cnt[i][d] = o + s + 1
                ans += s
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,4,6,8,10]
        o = 7
        self.assertEqual(s.numberOfArithmeticSlices(i), o)

    def test_two(self):
        s = Solution()
        i = [7,7,7,7,7]
        o = 16
        self.assertEqual(s.numberOfArithmeticSlices(i), o)

    def test_three(self):
        s = Solution()
        i = [1, 3, 5, 7, 9]
        o = 7
        self.assertEqual(s.numberOfArithmeticSlices(i), o)


if __name__ == '__main__':
    unittest.main(verbosity=2)