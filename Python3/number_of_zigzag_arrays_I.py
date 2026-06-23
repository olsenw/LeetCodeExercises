# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given three integers n, l, and r.

    A ZigZag array of length n is defined as follows:
    * Each element lies in the range [l, r].
    * No two adjacent elements are equal.
    * No three consecutive elements form a strictly increasing or strictly
      decreasing sequence.

    Return the total number of valid ZigZag arrays.

    Since the answer may be large, return it modulo 10^9 + 7.

    A sequence is said to be strictly increasing if each element is strictly
    greater than its previous one (if exists).

    A sequence is said to be strictly decreasing if each element is strictly
    smaller than its previous one (if exists).
    '''
    def zigZagArrays_tle(self, n: int, l: int, r: int) -> int:
        # endings = []
        @cache
        def dp(i:int, last:int, cur:int) -> int:
            if i == n:
                # endings.append((last,cur))
                return 1
            if last < cur:
                return sum((dp(i+1,cur,j) for j in range(cur-1,l-1,-1)))
            else:
                return sum(dp(i+1,cur,j) for j in range(cur+1,r+1))
            return 0
        answer = sum(dp(2,i,j) for i in range(l,r+1) for j in range(l,r+1) if i != j)
        return answer % (10**9 + 7)

    # based on hints
    def zigZagArrays_tle(self, n: int, l: int, r: int) -> int:
        @cache
        def dp(i:int, dir:int, x:int) -> int:
            if i == n:
                return 1
            dr = range(x-1,l-1,-1) if dir else range(x+1,r+1)
            return sum(dp(i+1, not dir, j) for j in dr)
        answer = sum(dp(1,1,i) for i in range(l,r+1))
        answer += sum(dp(1,0,i) for i in range(l,r+1))
        return answer % (10**9 + 7)

    # based on editorial
    # https://leetcode.com/problems/number-of-zigzag-arrays-i/editorial/?envType=daily-question&envId=2026-06-23
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = 10**9 + 7
        # range of values to consider
        workingRange = r - l + 1
        # dp array for decreasing values
        dpDown = [1] * workingRange
        # dp array for increasing values
        dpUp = [1] * workingRange
        # iterate length of generated array
        for _ in range(n-1):
            # prefix sum operation to make later calculation O(1)
            sumDown = list(accumulate(dpDown, initial=0))
            sumUp = list(accumulate(dpUp, initial=0))
            dpDown = [x % m for x in sumUp[:-1]]
            last = sumDown[-1]
            dpUp = [(last - x) % m for x in sumDown[1:]]
        return (sum(dpDown) + sum(dpUp)) % m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3,4,5
        o = 2
        self.assertEqual(s.zigZagArrays(*i), o)

    def test_two(self):
        s = Solution()
        i = 3,1,3
        o = 10
        self.assertEqual(s.zigZagArrays(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)