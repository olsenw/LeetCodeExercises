# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given 3 positive integers zero, one, and limit.

    A binary array arr is called stable if:
    * The number of occurrences of a 0 in arr is exactly zero.
    * The number of occurrences of a 1 in arr is exactly one.
    * Each subarray of arr with a size greater than limit must contain both 0
      and 1.
    
    Return the total number of stable binary arrays.

    Since the answer may be very large, return it modulo 10^9 + 7.
    '''
    # same solution as yesterday (problem #3129)
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # dp[a][b][c][d]
        # a is the number of zeros
        # b is the number of ones
        # c the last character is 0 or 1
        dp = [[[0,0] for _ in range(one + 1)] for _ in range(zero + 1)]
        mod = 10**9 + 7
        # it is only possible to have limit consecutive zeros
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        # it is only possible to have limit consecutive ones
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1
        # iterate over all possible zero one combinations
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # if more zeros than limits, remove all subarray with more zeros
                if i > limit:
                    dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1] - dp[i-limit-1][j][1]
                else:
                    dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
                dp[i][j][0] = (dp[i][j][0] % mod + mod) % mod
                # if more zeros than limits, remove all subarray with more zeros
                if j > limit:
                    dp[i][j][1] = dp[i][j-1][1] + dp[i][j-1][0] - dp[i][j-limit-1][0]
                else:
                    dp[i][j][1] = dp[i][j-1][1] + dp[i][j-1][0]
                dp[i][j][1] = (dp[i][j][1] % mod + mod) % mod
        return (dp[zero][one][0] + dp[zero][one][1]) % mod

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1,1,2
        o = 2
        self.assertEqual(s.numberOfStableArrays(*i), o)

    def test_two(self):
        s = Solution()
        i = 1,2,1
        o = 1
        self.assertEqual(s.numberOfStableArrays(*i), o)

    def test_three(self):
        s = Solution()
        i = 3,3,2
        o = 14
        self.assertEqual(s.numberOfStableArrays(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)