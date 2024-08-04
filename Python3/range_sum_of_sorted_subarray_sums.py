# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given the array nums consisting of n positive integers. Compute the sum of
    all non-empty continuous subarrays from the array and then sort them in
    non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

    Return the sum of the numbers from index left to index right (indexed from
    1), inclusive, in the new array. Since the answer can be large, return it
    modulo 10^9 + 7.
    '''
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        subarray = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                subarray.append(s)
        subarray.sort()
        return sum(subarray[left-1:right]) % (10**9 + 7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4], 4, 1, 5
        o = 13
        self.assertEqual(s.rangeSum(*i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4], 4, 3, 4
        o = 6
        self.assertEqual(s.rangeSum(*i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4], 4, 1, 10
        o = 50
        self.assertEqual(s.rangeSum(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)