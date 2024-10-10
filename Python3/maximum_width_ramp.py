# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A ramp in an integer array nums is a pair (i,j) for which i < j and
    nums[i] <= nums[j]. The width of such a ramp is j - i.

    Given an integer array nums, return the maximum width of a ramp in nums. If
    there is no ramp in nums, return 0.
    '''
    def maxWidthRamp_brute(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] <= nums[i]:
                    answer = max(i - j, answer)
                    break
        return answer

    def maxWidthRamp_fails(self, nums: List[int]) -> int:
        answer = 0
        mono = []
        for i in range(len(nums)):
            while mono and mono[-1][0] >= nums[i]:
                mono.pop()
            mono.append((nums[i], i))
            answer = max(answer, mono[-1][1] - mono[0][1])
        return answer

    # based on leetcode editorial
    # https://leetcode.com/problems/maximum-width-ramp/editorial/?envType=daily-question&envId=2024-10-10
    def maxWidthRamp(self, nums: List[int]) -> int:
        answer = 0
        mono = []
        for i in range(len(nums)):
            if not mono or nums[mono[-1]] > nums[i]:
                mono.append(i)
        for j in range(len(nums) - 1, -1, -1):
            while mono and nums[mono[-1]] <= nums[j]:
                answer = max(answer, j - mono[-1])
                mono.pop()
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [6,0,8,2,1,5]
        o = 4
        self.assertEqual(s.maxWidthRamp(i), o)

    def test_two(self):
        s = Solution()
        i = [9,8,1,0,1,9,4,0,4,1]
        o = 7
        self.assertEqual(s.maxWidthRamp(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)