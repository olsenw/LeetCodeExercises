# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. Transform nums by performing the following
    operations in the exact order specified:
    * Replace each even number with 0.
    * Replace each odd number with 1.
    * Sort the modified array in non-decreasing order.

    Return the resulting array after performing these operations.
    '''
    def transformArray(self, nums: List[int]) -> List[int]:
        odd = sum(n%2 for n in nums)
        return ([0] * (len(nums) - odd)) + ([1] * odd)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,3,2,1]
        o = [0,0,1,1]
        self.assertEqual(s.transformArray(i), o)

    def test_two(self):
        s = Solution()
        i = [1,5,1,4,2]
        o = [0,0,1,1,1]
        self.assertEqual(s.transformArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)