# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of distinct positive integers. Sort the array in
    increasing order based on the sum of the digits of each number. If two
    numbers have the same digit sum, the smaller number appears first in the
    sorted order.

    Return the minimum number of swaps required to rearrange nums into the
    sorted order.

    A swap is defined as exchanging the values at two distinct positions in the
    array.
    '''
    def minSwaps_hints(self, nums: List[int]) -> int:
        def digitSum(num:int) -> int:
            answer = 0
            while num:
                answer += num % 10
                num //= 10
            return answer
        # hint one find the sorted order of the array
        s = sorted([digitSum(j), j, i] for i,j in enumerate(nums))
        # hint two find minimum number of swaps to sort mapped array
        # which will be n - number_of_cycles in the permutation
        return

    # Based on Leetcode editorial
    # https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/editorial/?envType=daily-question&envId=2026-10-17
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        # calculate the digit sum for all indices
        digitSum = [0] * n
        for i,j in enumerate(nums):
            s = 0
            while j > 0:
                s += j % 10
                j //= 10
            digitSum[i] = s
        # sort the indices of nums based on digit sums
        indices = sorted((range(n)), key=lambda i: (digitSum[i], nums[i]))
        # track target position that swap needs to move
        target = [0] * n
        for i,j in enumerate(indices):
            target[j] = i
        # build graph and detect cycles
        # the graph should be 1:1 ideally, but cycles that link several are useful
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = target[j]
        # length of nums, but cycles reduce swaps needed
        return n - cycles

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [37,100]
        o = 1
        self.assertEqual(s.minSwaps(i), o)

    def test_two(self):
        s = Solution()
        i = [22,14,33,7]
        o = 0
        self.assertEqual(s.minSwaps(i), o)

    def test_three(self):
        s = Solution()
        i = [18,43,34,16]
        o = 2
        self.assertEqual(s.minSwaps(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)