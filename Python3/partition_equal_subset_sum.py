# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a non-empty array nums containing only positive integers find
    if the array can be partitioned into two subsets such that the sum
    of elements in both subsets is equal.
    '''
    def canPartition(self, nums: List[int]) -> bool:
        numsSum = sum(nums)
        if numsSum % 2 == 1:
            # if sum nums is odd it is impossible to get equal subarrays
            return False
        target = numsSum // 2
        if max(nums) > target:
            # element is larger than half sum nums, preventing equal sub
            return False
        '''
        name of the game from here on is dynamic programming
        '''
        # create dp array from 0 to target (target is included)
        dp = [False for i in range(target + 1)]
        # init base case (always able to get zero) (ie empty subarray)
        dp[0] = True
        # figure out summations of subarrays w/o element in nums
        for element in nums:
            # see what values can be reached between 0 and target
            for i in range(target, element - 1, -1):
                # does this element hit early value between 0 to target
                # will always hit case of dp[0]
                if dp[i - element]:
                    # save that this is reachable number for latter
                    dp[i] = True
                    # if we can add up to target the subarrays are valid
                    if dp[target]:
                        return True
        # unable to divide into subarrays
        return False

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        self.assertEqual(s.canPartition([1,5,11,5]), True)
    def test_two(self):
        s = Solution()
        self.assertEqual(s.canPartition([1,2,3,5]), False)
    def test_three(self):
        s = Solution()
        self.assertEqual(s.canPartition([7,8,11,4,1,1]), True)
    def test_four(self):
        s = Solution()
        self.assertEqual(s.canPartition([6,11,6,7,6]), True)

if __name__ == '__main__':
    unittest.main(verbosity=2)