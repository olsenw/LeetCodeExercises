# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    In one move, it is possible to increase the value of any single element
    nums[i] by 1.

    Return the minimum total number of moves required so that all elements in
    nums become equal.
    '''
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        return sum(m - i for i in nums)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,3]
        o = 3
        self.assertEqual(s.minMoves(i), o)

    def test_two(self):
        s = Solution()
        i = [4,4,5]
        o = 2
        self.assertEqual(s.minMoves(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)