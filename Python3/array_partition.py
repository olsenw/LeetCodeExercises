# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of 2n integers, group these integers into n
    pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai,bi) for
    all i is maximized. Return the maximized sum. 
    '''
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4,3,2]
        o = 4
        self.assertEqual(s.arrayPairSum(i), o)

    def test_two(self):
        s = Solution()
        i = [6,2,6,5,1,2]
        o = 9
        self.assertEqual(s.arrayPairSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)