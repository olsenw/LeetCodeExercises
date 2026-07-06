# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of odd length n.

    Return true if the middle element of nums appears exactly once in the array.
    Otherwise return false.
    '''
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        t = nums[len(nums) // 2]
        return sum(n == t for n in nums) == 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = True
        self.assertEqual(s.isMiddleElementUnique(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,2]
        o = False
        self.assertEqual(s.isMiddleElementUnique(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)