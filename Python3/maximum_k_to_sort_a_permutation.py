# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n, where nums is a permutation of the
    numbers in the range [0..n-1].

    It is possible to swap elements at indices i and j only if
    nums[i] AND nums[j] == k, where AND denotes the bitwise AND operation and k
    is a non-negative integer.

    Return the maximum value of k such that the array can be sorted in
    non-decreasing order using any number of such swaps. If nums is already
    sorted, return 0.
    '''
    # based on hint
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        answer = (1 << n.bit_length()) - 1
        for i,j in enumerate(nums):
            if i != j:
                answer &= i
        return answer if answer < n else 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,3,2,1]
        o = 1
        self.assertEqual(s.sortPermutation(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,3,2]
        o = 2
        self.assertEqual(s.sortPermutation(i), o)

    def test_three(self):
        s = Solution()
        i = [3,2,1,0]
        o = 0
        self.assertEqual(s.sortPermutation(i), o)

    def test_four(self):
        s = Solution()
        i = [0,1]
        o = 0
        self.assertEqual(s.sortPermutation(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)