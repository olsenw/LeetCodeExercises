# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums of length n and an integer target,
    return the number of pairs (i,j) where 0 <= i < j < n and
    nums[i] + nums[j] < target.
    '''
    def countPairs(self, nums: List[int], target: int) -> int:
        return sum(nums[i] + nums[j] < target for i in range(len(nums)) for j in range(i+1, len(nums)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-1,1,2,3,1]
        j = 2
        o = 3
        self.assertEqual(s.countPairs(i,j), o)

    def test_two(self):
        s = Solution()
        i = [-6,2,5,-2,-7,-1,3]
        j = -2
        o = 10
        self.assertEqual(s.countPairs(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)