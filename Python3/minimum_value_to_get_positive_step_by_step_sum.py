# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums, start with an initial positive value
    startValue.

    In each iteration, calculate the step by step sum of startValue plus
    elements in nums (from left to right).

    Return the minimum positive value of startValue such that the step by step
    sum is never less than 1.
    '''
    # hint helps a lot
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 10**7+1
        s = 0
        for n in nums:
            s += n
            startValue = min(startValue, s)
        return max(1, -startValue + 1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-3,2,-3,4,2]
        o = 5
        self.assertEqual(s.minStartValue(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        o = 1
        self.assertEqual(s.minStartValue(i), o)

    def test_three(self):
        s = Solution()
        i = [1,-2,-3]
        o = 5
        self.assertEqual(s.minStartValue(i), o)

    def test_four(self):
        s = Solution()
        i = [0,0,0]
        o = 1
        self.assertEqual(s.minStartValue(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)