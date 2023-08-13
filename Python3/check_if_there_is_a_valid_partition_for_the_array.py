# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums. Partition the array into one or more
    contiguous subarrays.

    A partition of the array is valid if each of the obtained subarrays
    satisfies one of the following conditions:
    1. The subarray consists of exactly 2 equal elements. For example, the
       subarray [2,2] is good.
    2. The subarray consists of exactly 3 equal elements. For example, the
       subarray [4,4,4] is good.
    3. The subarray consists of exactly 3 consecutive increasing elements, that
       is the difference between adjacent elements is 1. For example the
       subarray [3,4,5] is good, but the subarray [1,3,5] is not.

    Return true if the array has at least one valid partition. Otherwise return
    false.
    '''
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dp(i):
            if i == n:
                return True
            valid = False
            if i + 1 < n and nums[i] == nums[i+1]:
                valid |= dp(i+2)
            if i + 2 < n and nums[i] == nums[i+1] == nums[i+2]:
                valid |= dp(i+3)
            if i + 2 < n and nums[i] + 1 == nums[i+1] == nums[i+2] - 1:
                valid |= dp(i+3)
            return valid
        return dp(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,4,4,5,6]
        o = True
        self.assertEqual(s.validPartition(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,2]
        o = False
        self.assertEqual(s.validPartition(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1]
        o = True
        self.assertEqual(s.validPartition(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)