# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Given an integer array nums, handle multiple queries of the following type:

1. Calculate the sum of the elements of nums between the indices left and
   right inclusive where left <= right.

Implement the NumArray class:
'''
class NumArray:
    '''
    Initializes the object with the integer array nums.
    '''
    def __init__(self, nums: List[int]):
        self.nums = [0] + list(accumulate(nums))
        return

    '''
    Returns the sum of the elements of nums between indices left and right
    inclusive.
    '''
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(s.sumRange(0,2), 1)
        self.assertEqual(s.sumRange(2,5), -1)
        self.assertEqual(s.sumRange(0,5), -3)

if __name__ == '__main__':
    unittest.main(verbosity=2)