# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    Start by selecting a starting position curr such that nums[curr] == 0, and
    choose a movement direction of either left or right.

    After that, repeat the following process:
    * If curr is out of the range [0, n - 1], this process ends.
    * If nums[curr] == 0, move in the current direction by incrementing curr if
      moving right, or decrementing curr if moving left.
    * Else if nums[curr] > 0:
      * Decrement nums[curr] by 1.
      * Reverse movement direction (left becomes right and vice versa).
      * Take a step in new direction.
    
    A selection of the initial position curr and movement direction is
    considered valid if every element in nums becomes 0 by the end of the
    process.
    '''
    # brute force simulation
    def countValidSelections(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                values = list(nums)
                direction = True
                index = i
                while 0 <= index < len(nums):
                    if values[index] > 0:
                        values[index] -= 1
                        direction = not direction
                    if direction:
                        index += 1
                    else:
                        index -= 1
                if all(v == 0 for v in values):
                    answer += 1
                values = list(nums)
                direction = False
                index = i
                while 0 <= index < len(nums):
                    if values[index] > 0:
                        values[index] -= 1
                        direction = not direction
                    if direction:
                        index += 1
                    else:
                        index -= 1
                if all(v == 0 for v in values):
                    answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,0,2,0,3]
        o = 2
        self.assertEqual(s.countValidSelections(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,4,0,4,1,0]
        o = 0
        self.assertEqual(s.countValidSelections(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)