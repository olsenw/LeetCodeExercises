# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array nums of n integers and an integer target.

    Initially positioned at index 0. In one step, it is possible to jump from
    index i to any index j such that:
    * 0 <= i < j < n
    * -target <= nums[j] - nums[i] <= target

    Return the maximum number of jumps to make it to index n-1.

    If there is no way to reach index n-1, return -1.
    '''
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        jumps = defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                if abs(nums[j] - nums[i]) <= target:
                    jumps[i].append(j)
        # @cache
        # def dp(index:int) -> int:
        #     if index == n-1:
        #         return 1
        #     answer = -1
        #     for jump in jumps[index]:
        #         answer = max(answer, dp(jump))
        #     return answer
        answer = [-1] * n
        answer[-1] = 0
        for i in range(n-1,-1,-1):
            a = answer[i]
            for j in jumps[i]:
                if answer[j] > -1:
                    a = max(a, 1 + answer[j])
            answer[i] = a
        return answer[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,6,4,1,2]
        j = 2
        o = 3
        self.assertEqual(s.maximumJumps(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,3,6,4,1,2]
        j = 3
        o = 5
        self.assertEqual(s.maximumJumps(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,3,6,4,1,2]
        j = 0
        o = -1
        self.assertEqual(s.maximumJumps(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)