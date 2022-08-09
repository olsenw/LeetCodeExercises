# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of distinct integers nums and a target integer
    target, return the number of possible combinations that add up to
    target.

    The test cases are generated so that the answer can fit in a 32-bit
    integer.
    '''
    # bottom up solution based on discussion post by FreeTymeKiyan
    # https://leetcode.com/problems/combination-sum-iv/discuss/85036/1ms-Java-DP-Solution-with-Detailed-Explanation
    # problem should be about permutations because order matters...
    def combinationSum4(self, nums: List[int], target: int) -> int:
        do = [0] * (target + 1)
        do[0] = 1
        for i in range(target + 1):
            for n in nums:
                if i - n >= 0:
                    do[i] += do[i - n]
        return do[target]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        j = 4
        o = 7
        self.assertEqual(s.combinationSum4(i,j), o)

    def test_two(self):
        s = Solution()
        i = [9]
        j = 3
        o = 0
        self.assertEqual(s.combinationSum4(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)