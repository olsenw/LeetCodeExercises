# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice plays the following game, loosely based on the card game "21".

    Alice starts with 0 points and draws numbers while she has less than k
    points. During each draw, she gains an integer number of points randomly
    from range [1, maxPts], where maxPts is an integer. Each draw is independent
    and the outcomes have equal probabilities.

    Alice stops drawing numbers when she gets k or more points.

    Return the probability that Alice has n or fewer points.
    '''
    def new21Game_incorrect(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (k + maxPts) # [0, k+maxPts-1]
        for i in range(k):
            for j in range(1, maxPts + 1):
                dp[i + j] += 1
        return sum(dp[k:n+1]) / sum(dp[k:])
        # return sum(dp[:n+1]) / sum(dp)

    # O(n * maxPts) time (some accuracy issues)
    # derived from Leetcode solution
    def new21Game_slow(self, n: int, k: int, maxPts: int) -> float:
        # chance of having exactly dp[i] points
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, maxPts + 1):
                if i - j >= 0 and i - j < k:
                    dp[i] += dp[i - j] / maxPts
        return sum(dp[k:])

    # makes use of sliding window
    # derived from leetcode solution
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1
        s = 1 if k > 0 else 0
        for i in range(1, n+1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i - maxPts]
        return sum(dp[k:])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10
        j = 1
        k = 10
        o = 1.00
        self.assertEqual(s.new21Game(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 6
        j = 1
        k = 10
        o = 0.60
        self.assertEqual(s.new21Game(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 21
        j = 17
        k = 10
        o = 0.73278
        self.assertEqual(s.new21Game(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 10
        j = 2
        k = 10
        o = 0.99
        self.assertEqual(s.new21Game(i,j,k), o)

    def test_five(self):
        s = Solution()
        i = 6
        j = 2
        k = 10
        o = 0.55
        self.assertEqual(s.new21Game(i,j,k), o)

    def test_six(self):
        s = Solution()
        i = 6
        j = 3
        k = 10
        o = 0.484
        self.assertEqual(s.new21Game(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)