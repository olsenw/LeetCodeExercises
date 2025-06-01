# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two positive integers n and limit.

    Return the total number of ways to distribute n candies among 3 children
    such that no child get more than limit candies.
    '''
    def distributeCandies_brute(self, n: int, limit: int) -> int:
        answer = 0
        for i in range(min(n, limit) + 1):
            for j in range(min(n-i,limit) + 1):
                for k in range(min(n-i-j,limit)+1):
                    if i + j + k == n:
                        answer += 1
        return answer

    def distributeCandies_wrong(self, n: int, limit: int) -> int:
        # https://math.stackexchange.com/questions/5016883/calculate-ways-to-split-n-identical-items-into-m-groups-that-may-be-empty
        # the math
        answer = 0
        for i in range(min(n, limit + 1)):
            # give child one i candies (x candies remain)
            x = n - i
            # unable to split all candy between two children
            if x > 2 * limit:
                continue
            # need to spilt the x candies between two children
            y = (2 * limit) - x
            answer += math.factorial(y + 1) // math.factorial(y)
        return answer

    def distributeCandies_tle(self, n: int, limit: int) -> int:
        # https://math.stackexchange.com/questions/5016883/calculate-ways-to-split-n-identical-items-into-m-groups-that-may-be-empty
        # the math
        answer = 0
        for i in range(min(n, limit) + 1):
            # give child one i candies (x candies remain)
            x = n - i
            # unable to split all candy between two children
            if x > 2 * limit:
                continue
            if x == 2 * limit:
                answer += 1
                continue
            if x > limit:
                x -= 2 * (x - limit)
            answer += math.factorial(x + 1) // math.factorial(x)
        return answer

    # based on hints
    def distributeCandies(self, n: int, limit: int) -> int:
        return sum(max(0, min(limit, n-i) - max(0, n-i-limit) + 1) for i in range(min(n,limit)+1))
        answer = 0
        for i in range(min(n, limit) + 1):
            answer += max(0, min(limit, n-i) - max(0, n - i - limit) + 1)
        return answer

    # based on editorial
    # https://leetcode.com/problems/distribute-candies-among-children-ii/submissions/1650217795/?envType=daily-question&envId=2025-06-01
    def distributeCandies_constant(self, n: int, limit: int) -> int:
        def cal(x):
            if x < 0:
                return 0
            return x * (x - 1) // 2
        # total number of distributions
        a = cal(n + 2)
        # one child more than limit candies
        # note three ways to choose one child
        b = cal(n - limit + 1)
        # two children more than limit candies
        # note three ways to choose two children
        c = cal(n - 2 * (limit + 1) + 2)
        # all children more than limit candies
        d = cal(n - 3 * (limit + 1) + 2)
        # all together
        return a - (3 * b) + (3 * c) - d

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5, 2
        o = 3
        self.assertEqual(s.distributeCandies(*i), o)

    def test_two(self):
        s = Solution()
        i = 3, 3
        o = 10
        self.assertEqual(s.distributeCandies(*i), o)

    def test_three(self):
        s = Solution()
        i = 4, 3
        o = 12
        self.assertEqual(s.distributeCandies(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)