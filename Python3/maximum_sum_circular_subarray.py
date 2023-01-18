# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a circular integer array nums of length n, return the maximum possible
    sum of a non-empty subarray of nums.
    '''
    # copied from Leetcode solution, comment by Burntt
    # https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/2868539/maximum-sum-circular-subarray/?orderBy=most_votes
    # makes use of Kadane's algorithm
    # https://leetcode.com/problems/maximum-subarray/solutions/1126554/maximum-subarray/?orderBy=most_votes
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # init variables
        arraySum = 0
        currentMax = -math.inf
        bestMax = -math.inf
        currentMin = math.inf
        bestMin = math.inf
        # Kadane's algorithm
        for i in range(len(nums)):
            # compute sum of whole array
            arraySum += nums[i]
            # find maximum subarray sum
            currentMax = max(currentMax + nums[i], nums[i])
            bestMax = max(bestMax, currentMax)
            # find minimum subarray sum
            currentMin = min(currentMin + nums[i], nums[i])
            bestMin = min(bestMin, currentMin)
        # check if whole array was negative
        if bestMin == arraySum:
            return bestMax
        # return max
        return max(bestMax, arraySum - bestMin)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,-2,3,-2]
        o = 3
        self.assertEqual(s.maxSubarraySumCircular(i), o)

    def test_two(self):
        s = Solution()
        i = [5,-3,5]
        o = 10
        self.assertEqual(s.maxSubarraySumCircular(i), o)

    def test_three(self):
        s = Solution()
        i = [-3,-2,-3]
        o = -2
        self.assertEqual(s.maxSubarraySumCircular(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)