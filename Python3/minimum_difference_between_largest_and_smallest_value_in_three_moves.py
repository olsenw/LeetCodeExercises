# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    In one move, choose one element of nums and change it to any value.

    Return the minimum difference between the largest and smallest value of nums
    after performing at most three moves.
    '''
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        answer = min(
            nums[-4] - nums[0],
            nums[-3] - nums[1],
            nums[-2] - nums[2],
            nums[-1] - nums[3],
        )
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,3,2,4]
        o = 0
        self.assertEqual(s.minDifference(i), o)

    def test_two(self):
        s = Solution()
        i = [1,5,0,10,14]
        o = 1
        self.assertEqual(s.minDifference(i), o)

    def test_three(self):
        s = Solution()
        i = [3,100,20]
        o = 0
        self.assertEqual(s.minDifference(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)