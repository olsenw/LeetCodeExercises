# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums, return the number of good pairs.

    A pair (i, j) is called good if nums[i] == nums[j] and i < j.
    '''
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(nums[i] == nums[j] for i in range(len(nums)) for j in range(i+1, len(nums)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,1,1,3]
        o = 4
        self.assertEqual(s.numIdenticalPairs(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1]
        o = 6
        self.assertEqual(s.numIdenticalPairs(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3]
        o = 0
        self.assertEqual(s.numIdenticalPairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)