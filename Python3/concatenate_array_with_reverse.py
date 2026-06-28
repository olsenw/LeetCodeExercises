# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n.

    Construct a new array ans of length 2*n such that the first n elements are
    the same as nums, and the next n elements are the elements of nums in
    reverse order.

    Formally, for 0 <= i <= n - 1:
    * ans[i] = nums[i]
    * ans[i+n] = nums[n-i-1]

    Return an integer array ans.
    '''
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = [1,2,3,3,2,1]
        self.assertEqual(s.concatWithReverse(i), o)

    def test_two(self):
        s = Solution()
        i = [1]
        o = [1,1]
        self.assertEqual(s.concatWithReverse(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)