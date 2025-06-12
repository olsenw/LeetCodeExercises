# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a circular array nums, find the maximum absolute difference between
    adjacent elements.

    Note in a circular array, the first and last elements are adjacent.
    '''
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(nums[0])
        return max(abs(nums[i] - nums[i+1]) for i in range(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,4]
        o = 3
        self.assertEqual(s.maxAdjacentDistance(i), o)

    def test_two(self):
        s = Solution()
        i = [-5,-10,-5]
        o = 5
        self.assertEqual(s.maxAdjacentDistance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)