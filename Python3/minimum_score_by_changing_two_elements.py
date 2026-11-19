# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.
    * The low score of nums is the minimum absolute difference between any two
      integers.
    * The high score of nums is the maximum absolute difference between any two
      integers.
    * The score of nums is the sum of the high and low scores.

    Return the minimum score after changing two elements of nums.
    '''
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = nums[-1] - nums[2]
        answer = min(answer, nums[-2] - nums[1])
        answer = min(answer, nums[-3] - nums[0])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4,7,8,5]
        o = 3
        self.assertEqual(s.minimizeSum(i), o)

    def test_two(self):
        s = Solution()
        i = [1,4,3]
        o = 0
        self.assertEqual(s.minimizeSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)