# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer target.

    Return the number of subarrays of nums in which target is the majority
    element.

    The majority element of a subarray is the element that appears strictly more
    than half of the times in that subarray.
    '''
    # Based on leetcode editorial
    # https://leetcode.com/problems/count-subarrays-with-majority-element-ii/editorial/?envType=daily-question&envId=2026-06-26
    # convert each element into +! if nums[i] == target or -1 if nums[i] != target
    # track the prefix sum for each converted element
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # the possible answer range is [-n, n] map it to array
        values = [0] * (2 * n + 1)
        values[n] = 1
        # prefix sum
        count = n
        answer = 0
        presum = 0
        # iterate and prefix sum, use values to track previous subarrays
        for i in range(n):
            if nums[i] == target:
                presum += values[count]
                count += 1
                values[count] += 1
            else:
                count -= 1
                presum -= values[count]
                values[count] += 1
            answer += presum
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,3]
        j = 2
        o = 5
        self.assertEqual(s.countMajoritySubarrays(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1]
        j = 1
        o = 10
        self.assertEqual(s.countMajoritySubarrays(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3]
        j = 4
        o = 0
        self.assertEqual(s.countMajoritySubarrays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)