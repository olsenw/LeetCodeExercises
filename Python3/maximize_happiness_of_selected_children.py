# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array happiness of length n, and a positive integer k.

    There are n children standing in a queue, where the ith child has happiness
    value happiness[i]. Select k children from these n children in k turns.

    In each turn, when a child is selected, the happiness value of all the
    children that have not been selected till now decreases by 1. Note that the
    happiness value cannot become negative and gets decremented only if it is
    positive.

    Return the maximum sum of the happiness values of the selected children that
    can be achieved by selecting k children.
    '''
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        return sum(max(happiness[i] - i, 0) for i in range(k))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        j = 2
        o = 4
        self.assertEqual(s.maximumHappinessSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1]
        j = 2
        o = 1
        self.assertEqual(s.maximumHappinessSum(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2,3,4,5]
        j = 1
        o = 5
        self.assertEqual(s.maximumHappinessSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)