# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n, where nums is a permutation of the
    numbers in the range [1,n].

    A XOR triplet is defined as the XOR of three elements
    nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

    Return the number of unique XOR triplet values from all possible triplets
    (i, j, k).
    '''
    # based on Leetcode editorial
    # https://leetcode.com/problems/number-of-unique-xor-triplets-i/editorial/?envType=daily-question&envId=2026-07-23
    # can also see this if try enough test cases
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        b = 1
        while b <= len(nums):
            b *= 2
        return b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2]
        o = 2
        self.assertEqual(s.uniqueXorTriplets(i), o)

    def test_two(self):
        s = Solution()
        i = [3,1,2]
        o = 4
        self.assertEqual(s.uniqueXorTriplets(i), o)

    # def test_three(self):
    #     s = Solution()
    #     i = [3,1,2]
    #     o = 4
    #     self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)