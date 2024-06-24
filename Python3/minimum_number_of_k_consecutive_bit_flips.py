# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary array nums and an integer k.

    A k-bit flip is choosing a subarray of length k from nums and simultaneously
    changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

    Return the minimum number of k-bit flips required so that there is no 0 in
    the array. If it is not possible, return -1.

    A subarray is a contiguous part of an array.
    '''
    # based on Leetcode constant space solution
    # https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/editorial/?envType=daily-question&envId=2024-06-24
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        c = 0
        a = 0
        for i in range(len(nums)):
            if i >= k and nums[i-k] == 2:
                c -= 1
            if c % 2 == nums[i]:
                if i + k > len(nums):
                    return -1
                nums[i] = 2
                c += 1
                a += 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,0]
        j = 1
        o = 2
        self.assertEqual(s.minKBitFlips(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,0]
        j = 3
        o = -1
        self.assertEqual(s.minKBitFlips(i,j), o)

    def test_three(self):
        s = Solution()
        i = [0,0,0,1,0,1,1,0]
        j = 3
        o = 3
        self.assertEqual(s.minKBitFlips(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)