# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums of size n, return the minimum number of
    moves required to make all array elements equal.

    In one move, an element of the array may incremented or decremented
    by 1.

    Test cases are designed so that the answer will fit in a 32-bit int.
    '''
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        a = 0
        for i in range(len(nums)):
            a += abs(nums[i] - median)
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = 2
        self.assertEqual(s.minMoves2(i), o)

    def test_two(self):
        s = Solution()
        i = [1,10,2,9]
        #   2 10 2 9 - 1  |  9 10 2 9 - 8
        #   2 2  2 9 - 8  |  9 9  2 9 - 1
        #   2 2  2 2 - 7  |  9 9  9 9 - 7
        o = 16
        self.assertEqual(s.minMoves2(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)