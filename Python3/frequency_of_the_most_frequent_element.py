# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The frequency of an element is the number of times it occurs in an array.

    Given an integer array nums and an integer k. In one operation, choose an
    index of nums and increment the element at that index by 1.

    Return the maximum possible frequency of an element after performing at most
    k operations.
    '''
    # O(n^2) times out (65/71 test cases)
    def maxFrequency_brute(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = 0
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            h = i - 1
            steps = k
            while h >= 0 and nums[i] - nums[h] <= steps:
                steps -= nums[i] - nums[h]
                h -= 1
            h += 1
            answer = max(answer, j - h)
            i = j
        return answer

    def maxFrequency_wrong(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = 0
        # last number, how many
        x,y = 0, 0
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            y = j - i + max(y (k // (nums[i] - x)))
            answer = max(answer, y)
            x = nums[i]
            i = j
        return answer

    # based on LeetCode solution
    # https://leetcode.com/problems/frequency-of-the-most-frequent-element/editorial/?envType=daily-question&envId=2023-11-18
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = 0
        i = 0
        # sum of the window
        c = 0
        # move window to the right
        for j in range(len(nums)):
            c += nums[j]
            # shrink window
            # (j - i + 1) * nums[j] is total if every element in window equaled current num
            # subtracting the current sum of the window is how much it needs incremented
            # shrink the window until this is possible
            while (j - i + 1) * nums[j] - c > k:
                c -= nums[i]
                i += 1
            # largest window so far
            answer = max(answer, j - i + 1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,4]
        j = 5
        o = 3
        self.assertEqual(s.maxFrequency(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,4,8,13]
        j = 5
        o = 2
        self.assertEqual(s.maxFrequency(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3,9,6]
        j = 2
        o = 1
        self.assertEqual(s.maxFrequency(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)