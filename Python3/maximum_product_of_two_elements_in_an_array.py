# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given the array of integers nums, choose two different indices i and j of
    the array. Return the maximum value of (nums[i] - 1, nums[j] - 1).
    '''
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)

    '''
    can be done with a heap of size two

    can be done with two loops to find the two largest numbers
    '''
class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,4,5,2]
        o = 12
        self.assertEqual(s.maxProduct(i), o)

    def test_two(self):
        s = Solution()
        i = [1,5,4,5]
        o = 16
        self.assertEqual(s.maxProduct(i), o)

    def test_three(self):
        s = Solution()
        i = [3,7]
        o = 12
        self.assertEqual(s.maxProduct(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)