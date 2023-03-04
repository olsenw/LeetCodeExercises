# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and two integers minK and maxK.

    A fixed-bound subarray of nums is a subarray that satisfies the following
    conditions:
    * The minimum value in the subarray is equal to minK.
    * The maximum value in the subarray is equal to maxK.

    Return the number of fixed-bound subarrays.

    A subarray is a contiguous part of an array.
    '''
    # brute force sliding window with extra steps
    def countSubarrays_brute(self, nums: List[int], minK: int, maxK: int) -> int:
        def fixedBound(values: List[int]) -> int:
            if not values:
                return 0
            answer = 0
            for window in range(1, len(values) + 1):
                c = Counter(values[0:window])
                if minK in c and maxK in c:
                    answer += 1
                for i in range(window, len(values)):
                    c[values[i - window]] -= 1
                    c[values[i]] += 1
                    if c[minK] and c[maxK]:
                        answer += 1
            return answer
        # running tally
        answer = 0
        c = []
        for n in nums:
            # if number is in valid range add it to check array
            if minK <= n <= maxK:
                c.append(n)
            # see how many fixed-bound subarrays are present in this subarray
            else:
                answer += fixedBound(c)
                c = []
        return answer + fixedBound(c)

    # based on LeetCode solution
    # https://leetcode.com/problems/count-subarrays-with-fixed-bounds/editorial/
    # really slick
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        minPos, maxPos, left = -1, -1, -1
        for i in range(len(nums)):
            # valid range
            if minK <= nums[i] <= maxK:
                if nums[i] == minK:
                    minPos = i
                if nums[i] == maxK:
                    maxPos = i
                answer += max(0, min(minPos, maxPos) - left)
            # invalid number
            else:
                left = i
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,5,2,7,5]
        j = 1
        k = 5
        o = 2
        self.assertEqual(s.countSubarrays(i,j,k), o)

    def test_two(self):
        s = Solution()
        for i,o in enumerate([3,6,10,15,21,28], 2):
            self.assertEqual(s.countSubarrays([1] * i, 1, 1), o)
 
    def test_three(self):
        s = Solution()
        i = [1] * 10000
        j = 1
        k = 1
        o = 50005000
        self.assertEqual(s.countSubarrays(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)