# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k.

    An integer h is called valid if all values in the array that are strictly
    greater than h are identical.

    It is possible to perform the following operation on nums:
    * select an integer h that is valid for the current values in nums.
    * For each index i where nums[i] > h, set nums[i] to h.

    Return the minimum number of operations required to make every element in
    nums equal to k. If it is impossible to make all elements equal to k, return
    -1.
    '''
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set(nums)
        if any(i < k for i in s):
            return -1
        if min(s) > k:
            return len(s)
        return len(s) - 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,2,5,4,5]
        j = 2
        o = 2
        self.assertEqual(s.minOperations(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,1,2]
        j = 2
        o = -1
        self.assertEqual(s.minOperations(i,j), o)

    def test_three(self):
        s = Solution()
        i = [9,7,5,3]
        j = 1
        o = 4
        self.assertEqual(s.minOperations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)