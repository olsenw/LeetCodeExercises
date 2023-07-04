# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums where every element appears three times except
    for one, which appears exactly once. Find the single element and return it.

    Solution must use constant extra space and have a linear runtime.
    '''
    # does not meet constant space requirement
    def singleNumber_counter(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i in c:
            if c[i] == 1:
                return i

    '''
    Based on discussion post by kshatriyas
    https://leetcode.com/problems/single-number-ii/solutions/3714928/bit-manipulation-c-java-python-beginner-friendly/
    '''

    # O(size of int * len(nums)) runtime
    def singleNumber_brute_bitmask(self, nums: List[int]) -> int:
        answer = 0
        # iterate for each bit in a 32-bit integer
        for i in range(32):
            # how many times does that bit appear in nums
            s = sum((j >> i) & 1 for j in nums)
            # if it is not three times must be part of the answer
            if s % 3:
                answer = answer | (1 << i)
        return answer

    def singleNumber(self, nums: List[int]) -> int:
        # bits that have appeared once
        ones = 0
        # bits that have appeared twice
        twos = 0
        for n in nums:
            # only store bits that have not seen before (ie first time)
            ones = ones ^ (n & ~twos)
            # only store bits that have been seen once before (ie 2nd time)
            twos = twos ^ (n & ~ones)
            # when seen a third time it is removed from both due to bit magic
        return ones

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,2,3,2]
        o = 3
        self.assertEqual(s.singleNumber(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,0,1,0,1,99]
        o = 99
        self.assertEqual(s.singleNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)