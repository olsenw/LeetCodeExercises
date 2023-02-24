# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an unsorted integer array nums, return the smallest missing positive
    integer.

    Implement a solution that runs in O(n) time and uses O(1) space.
    '''
    # incorrect takes O(n log n) time because of sort
    # does pass LeetCode however...
    def firstMissingPositive_invalid(self, nums: List[int]) -> int:
        nums.sort()
        index = 0
        while index < len(nums) and nums[index] < 1:
            index += 1
        if index == len(nums) or nums[index] > 1:
            return 1
        while index < len(nums) - 1:
            if nums[index] + 1 < nums[index + 1]:
                return nums[index] + 1
            index += 1
        return nums[-1] + 1

    # incorrect takes O(n) space because of set
    # does pass LeetCode however...
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in s:
                return i
        return len(nums) + 1

    # LeetCode hints
    # fails if records out of order case [2,1]
    def firstMissingPositive_close(self, nums: List[int]) -> int:
        # use nums array as a set of seen numbers
        for i in range(len(nums)):
            value = nums[i]
            nums[i] = 0
            # may clobber future values
            if 0 < value < len(nums) + 1:
                nums[value - 1] = 1
        # find the first missing number
        for i in range(len(nums)):
            if nums[i] == 0:
                return i + 1
        # no missing numbers found so plus one of last
        return len(nums) + 1

    # discussion post by Abhishek291013
    # https://leetcode.com/problems/first-missing-positive/solutions/3084474/python-swap-simple/?languageTags=python3
    # keeps preforming past swaps until correct (have to check to ensure time constraint...)
    def firstMissingPositive_discussion(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            v = nums[i] - 1
            # keep performing swaps till in order
            while 0 < nums[i] < len(nums) + 1 and nums[i] != nums[v]:
                nums[i],nums[v] = nums[v],nums[i]
                v = nums[i] - 1
        # find the first missing number
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i + 1
        # no missing numbers found so plus one of last
        return len(nums) + 1

    # discussion post by m0biu5
    # https://leetcode.com/problems/first-missing-positive/solutions/1206111/python-o-n-time-and-constant-space-solution/?languageTags=python3
    # adds additional information by counting numbers with addition array length
    def firstMissingPositive_discussion2(self, nums: List[int]) -> int:
        n = len(nums)
		# mark all invalid numbers (by making them larger than array size)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        # skip
        for i in range(n):
            # skip invalid numbers
            if abs(nums[i]) > n:
                continue
            # neat flippy magic
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        # validates found numbers
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        # all found so answer is one more than array size
        return n + 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,0]
        o = 3
        self.assertEqual(s.firstMissingPositive(i), o)

    def test_two(self):
        s = Solution()
        i = [3,4,-1,1]
        o = 2
        self.assertEqual(s.firstMissingPositive(i), o)

    def test_three(self):
        s = Solution()
        i = [7,8,9,11,12]
        o = 1
        self.assertEqual(s.firstMissingPositive(i), o)

    def test_four(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 6
        self.assertEqual(s.firstMissingPositive(i), o)

    def test_five(self):
        s = Solution()
        i = [1,2,3,4,6]
        o = 5
        self.assertEqual(s.firstMissingPositive(i), o)

    def test_six(self):
        s = Solution()
        i = [2,1]
        o = 3
        self.assertEqual(s.firstMissingPositive(i), o)

    def test_seven(self):
        s = Solution()
        i = [3,2,1]
        o = 4
        self.assertEqual(s.firstMissingPositive(i), o)

    def test_eight(self):
        s = Solution()
        i = [2,3,1]
        o = 4
        self.assertEqual(s.firstMissingPositive(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)