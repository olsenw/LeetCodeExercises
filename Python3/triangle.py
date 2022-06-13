# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a triangle array, return the minimum path sum from top to
    bottom.

    For each step, it is possible to move to an adjacent number of the
    row below. Formally, from index i on row j it is possible to move to
    index i or i + 1 on row j + 1.
    '''
    def minimumTotalf(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2],[3,4],[6,5,7],[4,1,8,3]]
        o = 11
        self.assertEqual(s.minimumTotal(i), o)

    def test_two(self):
        s = Solution()
        i = [[-10]]
        o = -10
        self.assertEqual(s.minimumTotal(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)