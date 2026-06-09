# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n and an integer k.

    Choose exactly k non-empty subarrays nums[l..r] of nums. Subarrays may
    overlap, and the exact subarray (same l and r) can be chosen more than once.

    The value of a subarray nums[l..r] is defined as:
    max(nums[l..r]) - min(nums[l..r]).

    The total value is the sum of values of all chosen subarrays.

    Return the maximum possible total value that can be achieved.
    '''
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2]
        j = 2
        o = 4
        self.assertEqual(s.maxTotalValue(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,2,5,1]
        j = 3
        o = 12
        self.assertEqual(s.maxTotalValue(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)