# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, in which exactly two elements appear only once
    and all the other elements appear exactly twice. Find the two elements that
    appear only once. The answer may be returned in any order.

    Write an algorithm that runs in linear runtime complexity and uses only
    constant extra space.
    '''
    # based on answer by zhiqing_xiao
    # https://leetcode.com/problems/single-number-iii/solutions/68900/accepted-c-java-o-n-time-o-1-space-easy-solution-with-detail-explanations/
    def singleNumber(self, nums: List[int]) -> List[int]:
        # find the XOR of the two single numbers
        x = 0
        for n in nums:
            x ^= n
        # find the last set bit
        x &= -x
        # two distinct groups one with bit set and one without bit set
        a,b = 0,0
        for n in nums:
            if n & x == 0:
                a ^= n
            else:
                b ^= n
        return [a,b]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)