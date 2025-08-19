# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import permutations
import math
import operator
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array cards of length 4. There are four cards, each
    containing a number in the range [1,9]. Arrange the numbers on these cards
    in a mathematical expression using the operators ['+", '-', '*', '/'] and
    the parentheses '(' and ')' to get the value 24.

    The following restrictions are in place:
    * The division operator '/' represents real division, not integer division.
    * Every operation done is between two numbers. In particular the '-'
      operator may not be used as a unary operator.
    * Numbers cannot be concatenated together.

    Return true if it is possible to get an expression that evaluates to 24, and
    false otherwise.
    '''
    def judgePoint24(self, nums):
        if len(nums) == 1:
            # precision issue for float
            # return nums[0] == 24
            return math.isclose(nums[0], 24)
        pass
        for i,j in permutations(range(len(nums)), 2):
            for op in [operator.add, operator.sub, operator.mul, operator.truediv]:
                if op is operator.truediv and nums[j] == 0:
                    continue
                value = op(nums[i], nums[j])
                arr = [value] + [nums[k] for k in range(len(nums)) if i != k and j != k]
                if self.judgePoint24(arr):
                    return True
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,1,8,7]
        o = True
        self.assertEqual(s.judgePoint24(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,1,2]
        o = False
        self.assertEqual(s.judgePoint24(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)