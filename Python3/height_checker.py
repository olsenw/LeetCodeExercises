# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A school is trying to take an annual photo of all the students. The students
    are asked to stand in a single file line in non-decreasing order by height.
    Let this ordering be represented by the integer array expected where
    expected[i] is the expected height of the ith student in line.

    Given an integer array heights representing the current order that the
    students are standing in. Each heights[i] is the height of the it student in
    line (0-indexed).

    Return the number of indices where heights[i] != expected[i].
    '''
    def heightChecker(self, heights: List[int]) -> int:
        return sum(i != j for i,j in zip(heights, sorted(heights)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,4,2,1,3]
        o = 3
        self.assertEqual(s.heightChecker(i), o)

    def test_two(self):
        s = Solution()
        i = [5,1,2,3,4]
        o = 5
        self.assertEqual(s.heightChecker(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 0
        self.assertEqual(s.heightChecker(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)