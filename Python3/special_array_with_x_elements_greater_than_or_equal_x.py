# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of non-negative integers. nums is considered special if
    there exists a number x such that there are exactly x numbers in nums that
    are greater than or equal to x.

    Notice that x does not have to be an element in nums.

    Return x if the array is special, otherwise, return -1. It can be proven
    that if nums is special, the value for x is unique.
    '''
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        j = 0
        for i in range(n+1):
            while j < n and nums[j] < i:
                j += 1
            if i == n - j:
                return i
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,5]
        o = 2
        self.assertEqual(s.specialArray(i), o)

    def test_two(self):
        s = Solution()
        i = [0,0]
        o = -1
        self.assertEqual(s.specialArray(i), o)

    def test_three(self):
        s = Solution()
        i = [0,4,3,0,4]
        o = 3
        self.assertEqual(s.specialArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)