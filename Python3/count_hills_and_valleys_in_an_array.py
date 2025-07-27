# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums. An index i is part of a hill in nums
    if the closest non-equal neighbors of i are smaller than nums[i]. Similarly,
    an index i is part of a valley in nums if the closest non-equal neighbors of
    i are larger than nums[i]. Adjacent indices i and j are part of the same
    hill or valley if nums[i] == nums[j].

    Note that for an index to be part of a hill or valley, it must have a
    non-equal neighbor on both the left and right of the index.

    Return the number of hills and valleys in nums.
    '''
    # does not handle repeating numbers well
    def countHillValley_fails(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1, len(nums) - 1):
            if nums[i-1] > nums[i] <= nums[i+1] or nums[i-1] < nums[i] >= nums[i+1]:
                answer += 1
        return answer

    def countHillValley(self, nums: List[int]) -> int:
        a = [nums[0]]
        for n in nums[1:]:
            if n != a[-1]:
                a.append(n)
        nums = a
        answer = 0
        for i in range(1, len(nums) - 1):
            if nums[i-1] > nums[i] <= nums[i+1] or nums[i-1] < nums[i] >= nums[i+1]:
                answer += 1
        return answer
    
    '''
    There are better ways to handle this using while loops to iterate through
    list and sub while loops at potential peaks and valleys
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,4,1,1,6,5]
        o = 3
        self.assertEqual(s.countHillValley(i), o)

    def test_two(self):
        s = Solution()
        i = [6,6,5,5,4,1]
        o = 0
        self.assertEqual(s.countHillValley(i), o)

    def test_three(self):
        s = Solution()
        i = [2,2,1,1]
        o = 0
        self.assertEqual(s.countHillValley(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)