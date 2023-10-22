# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums (0-indexed) and an integer k.

    The score of a subarray (i,j) is defined as
    min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a
    subarray where i <= k <= j.

    Return the maximum possible score of a good subarray.
    '''
    # O(n^2)
    def maximumScore_time_exceeded(self, nums: List[int], k: int) -> int:
        # find the min value for (i,k)
        for i in range(k+1,len(nums)):
            nums[i] = min(nums[i-1], nums[i])
        # find the min value for (k,j)
        for i in range(k-1,-1,-1):
            nums[i] = min(nums[i], nums[i+1])
        # find best answer for all good subarrays
        answer = nums[k]
        for i in range(k,-1,-1):
            for j in range(k,len(nums)):
                answer = max(answer, min(nums[i],nums[j]) * (j-i+1))
        return answer

    # based on greedy solution
    # https://leetcode.com/problems/maximum-score-of-a-good-subarray/editorial/?envType=daily-question&envId=2023-10-22
    def maximumScore(self, nums: List[int], k: int) -> int:
        i,j = k,k
        answer = nums[k]
        m = nums[k]
        while i > 0 or j < len(nums) - 1:
            if (nums[j+1] if j < len(nums) - 1 else 0) > (nums[i-1] if i > 0 else 0):
                j += 1
                m = min(m, nums[j])
            else:
                i -= 1
                m = min(m, nums[i])
            answer = max(answer, m * (j - i + 1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4,3,7,4,5]
        j = 3
        o = 15
        self.assertEqual(s.maximumScore(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,5,4,5,4,1,1,1]
        j = 0
        o = 20
        self.assertEqual(s.maximumScore(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)