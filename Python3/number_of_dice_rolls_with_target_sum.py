# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given n dice each with k faces numbered from 1 to k.

    Given three integers n, k, and target, return the number of possible ways
    (out of the k^n total ways) to roll the dice so the sum of the face-up
    numbers equals target. Since the answer may be too large return it modulo
    10^9 + 7.
    '''
    # leetcode hint helped a-lot on what states to track
    def numRollsToTarget_valid(self, n: int, k: int, target: int) -> int:
        @cache
        def dp(remain, total):
            if remain == 0:
                return 1 if total == target else 0
            return sum(dp(remain-1, total+i) for i in range(1,k+1))
        return dp(n,0) % (10**9 + 7)

    # modulo addition done correctly
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        m = 10**9 + 7
        @cache
        def dp(remain, total):
            if remain == 0:
                return 1 if total == target else 0
            rolls = 0
            for i in range(1,k+1):
                rolls = ((rolls % m) + (dp(remain-1, total+i) % m)) % m
            return rolls
        return dp(n,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = (1,6,3)
        o = 1
        self.assertEqual(s.numRollsToTarget(*i), o)

    def test_two(self):
        s = Solution()
        i = (2,6,7)
        o = 6
        self.assertEqual(s.numRollsToTarget(*i), o)

    def test_three(self):
        s = Solution()
        i = (30,30,500)
        o = 222616187
        self.assertEqual(s.numRollsToTarget(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)