# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from bisect import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums and an integer target.

    Return the number of non-empty subsequences of nums such that the sum of the
    minimum and maximum element in it is less than or equal to target. Since the
    answer may be large, return it modulo 10^9 + 7.
    '''
    # used hints
    # needed editorial to get the 2^x subsequences calculation
    def numSubseq(self, nums: List[int], target: int) -> int:
        m = 10**9 + 7
        nums.sort()
        answer = 0
        for i in range(len(nums)):
            j = bisect(nums, target - nums[i]) - 1
            if j >= i:
                answer += pow(2, j - i, m) # 2^(j - i) % m
        return answer % m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,5,6,7]
        j = 9
        o = 4
        self.assertEqual(s.numSubseq(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,3,6,8]
        j = 10
        o = 6
        self.assertEqual(s.numSubseq(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2,3,3,4,6,7]
        j = 12
        o = 61
        self.assertEqual(s.numSubseq(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)