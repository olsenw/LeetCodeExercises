# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    We stack glasses in a pyramid, where the first row has 1 glass, the
    second row has 2 glasses, and so on until the 100th row. Each glass
    holds one cup of champagne.

    Then, some champagne is poured into the first glass at the top. When
    the topmost glass is full, any excess liquid poured will fall
    equally to the glass immediately to the left and right of it. When
    those glasses become full, any excess champagne will fall equally to
    the left and right of those glasses, and so on. (A glass at the
    bottom row has its excess champagne fall on the floor.)

    After pouring a non-negative integer cups of champagne, return how
    full the jth glass in the ith row is (both i and j are 0-indexed.)
    '''
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0] + [poured] + [0]
        for i in range(query_row):
            dp = [0] + [0.5 * max(0, dp[j - 1] - 1) + 0.5 * max(0, dp[j] - 1) for j in range(1, len(dp))] + [0]
        return min(dp[query_glass + 1], 1.0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        p = 1
        i = 1
        j = 1
        o = 0.0
        self.assertEqual(s.champagneTower(p, i, j), o)

    def test_two(self):
        s = Solution()
        p = 2
        i = 1
        j = 1
        o = 0.5
        self.assertEqual(s.champagneTower(p, i, j), o)

    def test_three(self):
        s = Solution()
        p = 100000009
        i = 33
        j = 17
        o = 1.0
        self.assertEqual(s.champagneTower(p, i, j), o)

    def test_five(self):
        s = Solution()
        self.assertEqual(s.champagneTower(10, 0, 0), 1.0)
        self.assertEqual(s.champagneTower(10, 1, 1), 1.0)
        self.assertEqual(s.champagneTower(10, 2, 1), 1.0)
        self.assertEqual(s.champagneTower(10, 3, 0), 0.375)
        self.assertEqual(s.champagneTower(10, 3, 1), 1.0)
        self.assertEqual(s.champagneTower(10, 4, 0), 0.0)
        self.assertEqual(s.champagneTower(10, 4, 1), 0.3125)
        self.assertEqual(s.champagneTower(10, 4, 2), 0.625)
        self.assertEqual(s.champagneTower(10, 5, 0), 0.0)
        self.assertEqual(s.champagneTower(10, 5, 4), 0.0)

if __name__ == '__main__':
    unittest.main(verbosity=2)