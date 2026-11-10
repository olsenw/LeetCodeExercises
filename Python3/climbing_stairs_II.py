# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Climbing a staircase with n+1 steps numbered from 0 to n.

    Also given a 1-indexed integer array costs of length n, where costs[i] is
    the cost of step i.

    From step 1, it is possible to jump only to step i + 1, i + 2, or i + 3. The
    cost of jumping from step i to step j is defined as costs[j] + (j - i)^2.

    Start at step 0 with cost = 0.

    Return the minimum total coast to reach step n.
    '''
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs = [0] + costs
        @cache
        def dp(i:int) -> int:
            answer = 10**9 + 7
            if i == n:
                answer = 0
            for j in range(i+1,i+4):
                if j <= n:
                    answer = min(
                        answer,
                        costs[j] + (j-i)**2 + dp(j)
                    )
            return answer
        return dp(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [1,2,3,4]
        o = 13
        self.assertEqual(s.climbStairs(i,j), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = [5,1,6,2]
        o = 11
        self.assertEqual(s.climbStairs(i,j), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [9,8,3]
        o = 12
        self.assertEqual(s.climbStairs(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)