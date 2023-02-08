# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a 0-indexed array of integers nums of length n. The starting position
    is at nums[0].

    Each element of nums[i] represents the maximum length of a froward jump from
    index i. In other words, starting at nums[i] it is possible to jump to any
    nums[i + j] where:
    * 0 <= j <= nums[i]
    * i + j < n

    REturn the minimum number of jumps to reach nums[n-1]. The test cases are
    generated such that it is possible to reach nums[n-1].
    '''
    def jump_dp(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i: int) -> int:
            if i == n - 1:
                return 0
            # k = [10**5 if j == 0 else 1 + dp(i + j) for j in range(nums[i]+1) if i + j < n]
            return min(10**5 if j == 0 else 1 + dp(i + j) for j in range(nums[i]+1) if i + j < n)
        return dp(0)

    def jump_greedy(self, nums: List[int]) -> int:
        jumps = 0
        # range of indices to consider
        i,j = 0,0
        while j < len(nums)-1:
            # update possible range -> (best last round, best this round)
            i,j = j + 1, max(k + nums[k] for k in range(i,j+1))
            jumps += 1
        return jumps

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,1,1,4]
        o = 2
        self.assertEqual(s.jump(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,0,1,4]
        o = 2
        self.assertEqual(s.jump(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)