# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a set of distinct positive integers nums, return the largest subset
    answer such that every pair (answer[i], answer[j]) of elements in the subset
    satisfies:
    * answer[i] % answer[j] == 0, or
    * answer[j] % answer[i] == 0

    If there are multiple solutions, return any of them.
    '''
    # based on solution by MarkSPhilip31
    # https://leetcode.com/problems/largest-divisible-subset/solutions/4699685/beats-99-users-c-java-python-javascript-explained/?envType=daily-question&envId=2024-02-09
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        # dp array
        dp = [1] * n
        # longest possible subset, final index in the longest subset
        a,b = 1,0
        # iterate all pairs
        for i in range(1,n):
            for j in range(i):
                # if valid update dp array
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    # update if this is longest subset
                    if dp[i] > a:
                        a = dp[i]
                        b = i
        # backtrack to calculate answer
        answer = []
        c = nums[b]
        for i in range(b, -1, -1):
            if c % nums[i] == 0 and dp[i] == a:
                answer.append(nums[i])
                a -= 1
                c = nums[i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = [2,1]
        self.assertEqual(s.largestDivisibleSubset(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,4,8]
        o = [8,4,2,1]
        self.assertEqual(s.largestDivisibleSubset(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)