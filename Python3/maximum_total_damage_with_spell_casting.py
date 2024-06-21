# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    A magician has various spells.

    Given an array power, where each element represents the damage of a spell.
    Multiple spells can have the same damage value.

    It is a known fact that if a magician decides to cast a spell with a damage
    of power[i], they cannot cast any spell with a damage of power[i] - 2,
    power[i] - 1, power[i] + 1, or power[i] + 2.

    Each spell can be cast only once.

    Return the maximum possible total damage that a magician can cast.
    '''
    # memory limit exceeded
    def maximumTotalDamage_memory(self, power: List[int]) -> int:
        c = Counter(power)
        power = sorted(c.keys())
        n = len(power)
        @cache
        def dp(i,j):
            if i == n:
                return 0
            if power[i] <= j:
                return dp(i+1, j)
            return max(
                dp(i+1, power[i] + 2) + power[i] * c[power[i]],
                dp(i+1, j)
            )
        return dp(0, -2)

    # based on solution by lancertech6
    # https://leetcode.com/problems/maximum-total-damage-with-spell-casting/solutions/5320446/beats-100-explained-with-video-c-java-python-js-dynamic-programming-interview-solution/
    # has a linear dp instead or my square dp
    def maximumTotalDamage(self, power: List[int]) -> int:
        # frequency of all spell powers
        c = Counter(power)
        # sorted list of powers
        power = sorted(c.keys())
        # dp array
        n = len(power)
        dp = [0] * n
        # base case
        dp[0] = power[0] * c[power[0]]
        # for each unique spell power
        for i in range(1, n):
            # get value of current spell
            curr = power[i] * c[power[i]]
            # case where don't use current spell
            dp[i] = dp[i-1]
            # find last usable spell power
            j = i - 1
            while (j >= 0 and (
                power[j] == power[i] - 2 or
                power[j] == power[i] - 1 or
                power[j] == power[i] + 1 or
                power[j] == power[i] + 2)):
                j -= 1
            # if a previous usable spell power is found
            if j >= 0:
                # choice between leave or take current spell
                dp[i] = max(dp[i], dp[j] + curr)
            else:
                # choice between only using new spell or old spell
                dp[i] = max(dp[i], curr)
        return dp[-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,3,4]
        o = 6
        self.assertEqual(s.maximumTotalDamage(i), o)

    def test_two(self):
        s = Solution()
        i = [7,1,6,6]
        o = 13
        self.assertEqual(s.maximumTotalDamage(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = 1
        self.assertEqual(s.maximumTotalDamage(i), o)

    def test_four(self):
        s = Solution()
        i = [7,1,6,3]
        o = 10
        self.assertEqual(s.maximumTotalDamage(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)