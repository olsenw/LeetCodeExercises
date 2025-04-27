# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, return the number of subarrays of length 3 such
    that the sum of the first and third numbers equals exactly half of the
    second number.
    '''
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(2 * (nums[i-1] + nums[i+1]) == nums[i] for i in range(1, len(nums)-1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1,4,1]
        o = 1
        self.assertEqual(s.countSubarrays(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1]
        o = 0
        self.assertEqual(s.countSubarrays(i), o)

    def test_three(self):
        s = Solution()
        i = [0,-4,-4]
        o = 0
        self.assertEqual(s.countSubarrays(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)