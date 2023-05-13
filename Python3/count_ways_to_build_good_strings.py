# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given the integers zero, one, low, and high, a string can be constructed by
    starting with the empty string, and then at each step preform either of the
    following:
    * Append the character '0' 'zero' times.
    * Append the character '1' 'one' times.

    This step can be preformed any number of times.

    A good string is a string constructed by the above process having a length
    between low and high (inclusive).

    Return the number of different good strings that can be constructed
    satisfying these properties. Since the answer may be large, return it modulo
    10^9 + 7.
    '''
    # based on leetcode iterative solution
    # https://leetcode.com/problems/count-ways-to-build-good-strings/editorial/
    # really helps when you read the problem correctly...
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0] * high
        m = 10**9 + 7
        for i in range(1,high+1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= m
        return sum(dp[low:high+1]) % m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = (3,3,1,1)
        o = 8
        self.assertEqual(s.countGoodStrings(*i), o)

    def test_two(self):
        s = Solution()
        i = (2,3,1,2)
        o = 5
        self.assertEqual(s.countGoodStrings(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)