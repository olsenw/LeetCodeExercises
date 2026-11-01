# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of size n, return the minimum number of moves
    required to make all array elements equal.

    In one move it is possible to increment n-1 elements of the array by 1.
    '''
    def minMoves_fails(self, nums: list[int]) -> int:
        m,n = max(nums), min(nums)
        return 0 if m == n else m-n+1

    def minMoves_fails(self, nums: list[int]) -> int:
        c = Counter(nums)
        if len(c) == 1:
            return 0
        m = max(c)
        n = min(c)
        if len(c) == 2:
            return m - n
        return m - n + 1

    # based on solution by Aleksandr
    # https://leetcode.com/problems/minimum-moves-to-equal-array-elements/solutions/8596552/dont-simulate-solve-min-n-sum-closed-for-sdow/?envType=daily-question&envId=2026-11-01
    def minMoves(self, nums: list[int]) -> int:
        # goal is to have all the values of nums be equal
        #   * this is true when the sum of nums equals the length of the array * smallest value
        # each iteration does the following
        #   * adds 1 to the smallest value in the array
        #   * adds n-1 to the sum of all values
        # need to find a value k (number of operations) that makes this equal
        #   * (min(nums) + k) * len(nums) = sum(nums) + k * (len(nums) - 1)
        #   *                           k = sum(nums) - min(nums) * len(nums)
        return sum(nums) - len(nums) * min(nums)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = 3
        self.assertEqual(s.minMoves(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1]
        o = 0
        self.assertEqual(s.minMoves(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2]
        o = 1
        self.assertEqual(s.minMoves(i), o)

    def test_four(self):
        s = Solution()
        i = [-100,0,100]
        o = 300
        self.assertEqual(s.minMoves(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)