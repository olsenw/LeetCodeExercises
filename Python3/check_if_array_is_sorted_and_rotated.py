# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums, return true if the array was originally sorted in
    non-decreasing order, then rotated some number of positions (including
    zero). Otherwise, return False.

    There may be duplicates in the original array.

    Note: An array A rotated by x positions results in an array B of the same
    length such that A[i] == B[(i+x) % A.length], where % is the modulo
    operation.
    '''
    def check(self, nums: List[int]) -> bool:
        t = False
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                if t:
                    return False
                t = True
        if t and nums[0] < nums[-1]:
            return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,4,5,1,2]
        o = True
        self.assertEqual(s.check(i), o)

    def test_two(self):
        s = Solution()
        i = [2,1,3,4]
        o = False
        self.assertEqual(s.check(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3]
        o = True
        self.assertEqual(s.check(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)