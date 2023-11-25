# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums sorted in non-decreasing order.

    Build and return an integer array result with the same length as nums such
    that result[i] is equal to the summation of absolute differences between
    nums[i] and all the other elements in the array.

    In other words, result[i] is equal to sum(abs(nums[i] - nums[j])) where
    0 <= j < nums.length and j != i (0-indexed).
    '''
    # brute force O(n^2)
    def getSumAbsoluteDifferences_brute(self, nums: List[int]) -> List[int]:
        return [sum(abs(nums[i] - nums[j]) for j in range(len(nums))) for i in range(len(nums))]

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        for i in range(1, n):
            answer[i] = (nums[i] - nums[i-1]) * i + answer[i-1]
        s = nums[-1]
        for i in range(n - 2, -1, -1):
            answer[i] += s - (n - i - 1) * nums[i]
            s += nums[i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,5]
        o = [4,3,5]
        self.assertEqual(s.getSumAbsoluteDifferences(i), o)

    def test_two(self):
        s = Solution()
        i = [1,4,6,8,10]
        o = [24,15,13,15,21]
        self.assertEqual(s.getSumAbsoluteDifferences(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)