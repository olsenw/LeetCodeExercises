# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given the two integers m and n, return the number of possible unique
    paths that the robot can take to reach the bottom-right corner.

    The test cases are generated so that the answer will be less than or
    equal to 2 * 10^9.
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        m += 1
        n += 1
        dp = [[0] * n for _ in range(m)]
        dp[1][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = 7
        o = 28
        self.assertEqual(s.uniquePaths(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 2
        o = 3
        self.assertEqual(s.uniquePaths(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)