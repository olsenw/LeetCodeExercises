# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
from functools import cache
from math import comb
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string num. A string of digits is called balanced if the sum of the
    digits at even indices is equal to the sum of the digits at odd indices.

    Return the number of distinct permutations of num that are balanced.

    Since the answer may be very large, return it modulo 10^9 + 7.

    A permutation is a rearrangement of all the characters of a string.
    '''
    # based on leetcode solution
    # https://leetcode.com/problems/count-number-of-balanced-permutations/?envType=daily-question&envId=2025-05-09
    # lot of recursive permutation math
    def countBalancedPermutations(self, num: str) -> int:
        m = 10**9 + 7
        num = list(map(int, num))
        s = sum(num)
        if s % 2:
            return 0
        target = s // 2
        c = Counter(num)
        n = len(num)
        maxOdd = (n+1) // 2
        psum = [0] * 11
        for i in range(9, -1, -1):
            psum[i] = psum[i + 1] + c[i]
        @cache
        def dfs(pos, curr, oddCnt):
            # if illegal placement or sum odd is greater than target
            if oddCnt < 0 or psum[pos] < oddCnt or curr > target:
                return 0
            if pos > 9:
                return int(curr == target and oddCnt == 0)
            evenCnt = psum[pos] - oddCnt
            res = 0
            for i in range(max(0, c[pos] - evenCnt), min(c[pos], oddCnt) + 1):
                ways = comb(oddCnt, i) * comb(evenCnt, c[pos] - i) % m
                res += ways * dfs(pos + 1, curr + i * pos, oddCnt - i)
            return res % m
        return dfs(0,0,maxOdd)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "123"
        o = 2
        self.assertEqual(s.countBalancedPermutations(i), o)

    def test_two(self):
        s = Solution()
        i = "112"
        o = 1
        self.assertEqual(s.countBalancedPermutations(i), o)

    def test_three(self):
        s = Solution()
        i = "12345"
        o = 0
        self.assertEqual(s.countBalancedPermutations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)