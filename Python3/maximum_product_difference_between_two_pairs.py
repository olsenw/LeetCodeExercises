# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The product difference between two pairs (a,b) and (c,d) is defined as
    (a * b) - (c * d).

    Given an integer array nums, choose four distinct indices w, x, y, and z
    such that the product difference between pairs (nums[w],  nums[x]) and
    (nums[y], nums[z]) is maximized.

    Return the maximum such product difference
    '''
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,6,2,7,4]
        o = 34
        self.assertEqual(s.maxProductDifference(i), o)

    def test_two(self):
        s = Solution()
        i = [4,2,5,9,7,4,8]
        o = 64
        self.assertEqual(s.maxProductDifference(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)