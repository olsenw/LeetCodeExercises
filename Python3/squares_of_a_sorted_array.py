# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums sorted in non-decreasing order, return an array
    of the squares of each number sorted in non-decreasing order.
    '''
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(i * i for i in nums)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-4,-1,0,3,10]
        o = [0,1,9,16,100]
        self.assertEqual(s.sortedSquares(i), o)

    def test_two(self):
        s = Solution()
        i = [-7,-3,2,3,11]
        o = [4,9,9,49,121]
        self.assertEqual(s.sortedSquares(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)