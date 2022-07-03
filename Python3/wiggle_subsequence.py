# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from functools import cache

class Solution:
    '''
    A wiggle sequence is a sequence where the differences between
    successive numbers strictly alternate between positive and negative.
    The first difference (if one exists) may either be positive or
    negative. A sequence with one element and a sequence with two
    non-equal elements are trivially wiggle sequences.
    * For example [1,7,4,9,2,5] is a wiggle sequence because the
      differences (6,-3,5,-7,3) alternate between positive and negative.
    * In contrast [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences.
      The first because its first two differences are positive, and the
      second is not because its last difference is zero.

    A subsequence is obtained by deleting some elements (possibly zero)
    from the original sequence, leaving the remaining elements in their
    original order.

    Given an integer array nums, return the length of the longest wiggle
    subsequence of nums.
    '''
    # Base on Leetcode solution
    # Dynamic programming where testing combinations differences are
    # positive or negative and updating accordingly (ie for each element
    # update with the largest sequence that could include it)
    # O(n^2) time O(n) space
    # was really close to this one... could not work through bugs...
    def wiggleMaxLength_leetcode_dp(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        positive = [0] * len(nums)
        negative = [0] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    positive[i] = max(positive[i], negative[j] + 1)
                if nums[i] < nums[j]:
                    negative[i] = max(negative[i], positive[j] + 1)
        return 1 + max(positive[-1], negative[-1])

    '''
    Can optimize the above dp solution by checking if it is one of three
    cases (increasing, decreasing, equal) and updating both positive and 
    negative dp arrays accordingly (in tandem).

    Do that and it is possible to use constant space because only the
    tail of dp array is ever needed.
    '''

    # based on Leetcode solution
    # Counts the number of alternating max min peaks
    # O(n) time O(1) space
    def wiggleMaxLength_leetcode_greedy(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        pdiff = nums[1] - nums[0]
        count = 2 if pdiff != 0 else 1
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and pdiff <= 0) or (diff < 0 and pdiff >= 0):
                count += 1
                pdiff = diff
        return count

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,7,4,9,2,5]
        o = 6
        self.assertEqual(s.wiggleMaxLength(i), o)

    def test_two(self):
        s = Solution()
        i = [1,17,5,10,13,15,10,5,16,8]
        o = 7
        self.assertEqual(s.wiggleMaxLength(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5,6,7,8,9]
        o = 2
        self.assertEqual(s.wiggleMaxLength(i), o)

    def test_four(self):
        s = Solution()
        i = [1]
        o = 1
        self.assertEqual(s.wiggleMaxLength(i), o)

    def test_five(self):
        s = Solution()
        i = [1,2]
        o = 2
        self.assertEqual(s.wiggleMaxLength(i), o)

    def test_six(self):
        s = Solution()
        i = [1,1]
        o = 1
        self.assertEqual(s.wiggleMaxLength(i), o)

    def test_seven(self):
        s = Solution()
        i = [2,4,5,7,5,5,7,2,3]
        o = 6
        self.assertEqual(s.wiggleMaxLength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)