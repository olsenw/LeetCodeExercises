# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array nums consisting of positive integers.

    Initially, it is possible to increase the value of any element in the array
    by at most 1.

    Afterwards, select one or more elements from the final array such that those
    elements are consecutive when sorted in increasing order.

    Return the maximum number of elements that can be selected.
    '''
    # not solving the target problem
    def maxSelectedElements_invalid(self, nums: List[int]) -> int:
        nums.sort()
        dp = dict()
        i,j = 0,0
        a = 1
        while j < len(nums):
            if nums[i] + 1 == nums[j]:
                a += 1
            while nums[i] + 1 < nums[j]:
                if nums[i] not in dp:
                    dp[nums[i]] = a
                    a -= 1
                i += 1
            j += 1
        return

    def maxSelectedElements_closer(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        for n in nums:
            if n in s:
                s.add(n+1)
            s.add(n)
        nums = sorted(s)
        answer = 1
        i = 0
        for j in range(1, len(nums)):
            if nums[j-1] + 1 < nums[j]:
                answer = max(answer, j - i)
                i = j
        return max(answer, j - i)

    # brute force finding length of consecutive
    def maxSelectedElements_tle(self, nums: List[int]) -> int:
        nums.sort()
        o = set()
        s = set()
        for n in nums:
            if n in s:
                s.add(n+1)
            s.add(n)
            o.add(n)
        nums = list(s)
        n = len(nums)
        answer = 0
        for i in range(n):
            a = 1
            for k in range(i+1,n):
                if nums[k-1]+1 != nums[k]:
                    break
                a += 1
            answer = max(answer, a)
            if nums[i] in o:
                nums[i] += 1
            a = 1
            for k in range(i+1,n):
                if nums[k-1]+1 != nums[k]:
                    break
                a += 1
            answer = max(answer, a)
            pass
        return answer

    def maxSelectedElements_fails(self, nums: List[int]) -> int:
        nums.sort()
        o = set()
        s = set()
        for n in nums:
            # if n in s:
            s.add(n)
            s.add(n+1)
            o.add(n)
        nums = list(s)
        n = len(nums)
        @cache
        def dp(i:int) -> int:
            if i+1 < n and nums[i]+1 == nums[i+1]:
                return 1 + dp(i+1)
            return 1
        answer = 0
        for i in range(n):
            answer = max(answer, dp(i))
            if nums[i] in o:
                j = bisect.bisect_left(nums, nums[i] + 1)
                if j < n and nums[i] + 2 == nums[j]:
                    answer = max(answer, 1 + dp(j))
            pass
        return answer

    def maxSelectedElements_fails(self, nums: List[int]) -> int:
        nums.sort()
        last = nums[-1]
        @cache
        def dp(i:int) -> int:
            nonlocal last
            if i == 0:
                return 1
            if nums[i] == last:
                return dp(i-1)
            temp = last
            answer = 0
            if nums[i] + 1 == temp:
                last = nums[i]
                answer = max(answer, 1 + dp(i-1))
            if nums[i] + 2 == temp:
                last = nums[i] + 1
                answer = max(answer, 1 + dp(i-1))
            last = temp
            return answer
        answer = 0
        for i in range(len(nums) - 1, -1, -1):
            last = nums[i] + 1
            answer = max(answer, dp(i))
            last = nums
        return dp(len(nums) - 1)

    def maxSelectedElements_incomplete(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            x = nums[i]
            y = x + 1
        return

    # based on Leetcode editorial
    # https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/editorial/?envType=daily-question&envId=2026-11-20
    # notice how this does not play with indexes at all
    # works directly off of the current value being considered
    # the current value can do two things
    # 1) value + 1 is appended to longest sequence of ending in value
    # 2) value is appended to longest sequence of ending in value - 1
    # note it is important to process case 1 before case 2 as both need current element (ie double counting it)
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        dp = defaultdict(int)
        for n in nums:
            dp[n+1] = max(dp[n+1], 1 + dp[n])
            dp[n] = max(dp[n], 1 + dp[n-1])
            answer = max(answer, dp[n+1], dp[n])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,5,1,1]
        o = 3
        self.assertEqual(s.maxSelectedElements(i), o)

    def test_two(self):
        s = Solution()
        i = [1,4,7,10]
        o = 1
        self.assertEqual(s.maxSelectedElements(i), o)

    def test_three(self):
        s = Solution()
        i = [8,10,6,12,9,12,2,3,13,19,11,18,10,16]
        o = 8
        self.assertEqual(s.maxSelectedElements(i), o)

    def test_four(self):
        s = Solution()
        i = [12,11,8,7,2,10,18,12]
        o = 6
        self.assertEqual(s.maxSelectedElements(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)