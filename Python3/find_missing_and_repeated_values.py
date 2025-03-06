# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed 2D integer matrix grid of size n * n with values in the
    range [1, n^2]. Each integer appears exactly once except a which appears
    twice and b which is missing. The task is to find the repeating and missing
    numbers a and b.

    Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and
    ans[1] equals to b.
    '''
    # brute force because 1 <= n <= 50
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        double = 0
        s = set(range(1,(len(grid)**2)+1))
        for row in grid:
            for col in row:
                if col in s:
                    s.remove(col)
                else:
                    double = col
        return [double, s.pop()]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,3],[2,2]]
        o = [2,4]
        self.assertEqual(s.findMissingAndRepeatedValues(i), o)

    def test_two(self):
        s = Solution()
        i = [[9,1,7],[8,9,2],[3,4,6]]
        o = [9,5]
        self.assertEqual(s.findMissingAndRepeatedValues(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)