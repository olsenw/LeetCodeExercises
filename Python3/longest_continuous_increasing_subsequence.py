# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an unsorted array of integers nums, return the length of the longest
    continuous increasing subsequence (i.e. subarray). The subsequence must be
    strictly increasing.

    A continuous increasing subsequence is defined by two indices l and r 
    (l < r) such that it is [nums[l], nums[l+1], ..., nums[r-1], nums[r]] and
    for each l <= i < r, nums[i] < nums[i+1]
    '''
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        nums.append(-10**9-7)
        answer = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                answer = max(answer, curr)
                curr = 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,5,4,7]
        o = 3
        self.assertEqual(s.findLengthOfLCIS(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2,2,2,2]
        o = 1
        self.assertEqual(s.findLengthOfLCIS(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5,6,7]
        o = 7
        self.assertEqual(s.findLengthOfLCIS(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)