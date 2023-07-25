# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums and an integer threshold.

    Find the length of the longest subarray of nums starting at index 1 and
    ending at index r (0 <= l <= r < nums.length) that satisfies the following
    conditions:
    * nums[l] % 2 == 0
    * For all indices i in the range [l, r-1], nums[i] % 2 != nums[i+1] % 2
    * For all indices i in the range [l,r], nums[i] <= threshold.

    Return an integer denoting the length of the longest such subarray.

    Note: A subarray is a contiguous non-empty sequence of elements within an
    array.
    '''
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        answer = 0
        left = 0
        right = 1
        while left < len(nums):
            if nums[left] <= threshold and nums[left] % 2 == 0:
                right = left + 1
                flip = 1
                while right < len(nums) and nums[right] <= threshold and nums[right] % 2 == flip:
                    flip = 0 if flip == 1 else 1
                    right += 1
                answer = max(answer, right - left)
                left = right - 1
            left += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,5,4]
        j = 5
        o = 3
        self.assertEqual(s.longestAlternatingSubarray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        j = 2
        o = 1
        self.assertEqual(s.longestAlternatingSubarray(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2,3,4,5]
        j = 4
        o = 3
        self.assertEqual(s.longestAlternatingSubarray(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,3,4,5]
        j = 4
        o = 1
        self.assertEqual(s.longestAlternatingSubarray(i,j), o)

    def test_five(self):
        s = Solution()
        i = [1,3,4,5]
        j = 5
        o = 2
        self.assertEqual(s.longestAlternatingSubarray(i,j), o)

    def test_six(self):
        s = Solution()
        i = [4,10,3]
        j = 10
        o = 2
        self.assertEqual(s.longestAlternatingSubarray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)