# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A sequence x1,x2, ..., xn is Fibonacci like if:
    * n >= 3
    * xi + xi+1 == xi+2 for all i+2 <= n

    Given a strictly increasing array arr of positive integers forming a
    sequence, return the length of the longest Fibonacci like subsequence of
    arr. If one does not exist, return 0.

    A subsequence is derived from another sequence arr by deleting any number of
    elements (including none) from arr, without changing the order of the
    remaining elements.
    '''
    def lenLongestFibSubseq_wrong(self, arr: List[int]) -> int:
        values = {j:i for i,j in enumerate(arr)}
        @cache
        def dp(index:int) -> int:
            answer = 0
            for i in range(index-1,-1,-1):
                t = arr[index] - arr[i]
                if t in values:
                    answer = max(answer, 2 + min(1, dp(values[t])))
            return answer
        return dp(len(arr) - 1)

    def lenLongestFibSubseq_memory_limit(self, arr: List[int]) -> int:
        values = {j:i for i,j in enumerate(arr)}
        @cache
        def dp(a:int, b:int) -> int:
            if a + b in values:
                return 1 + dp(b, a+b)
            return 0
        n = len(arr)
        answer = 0
        for i in range(n):
            for j in range(i+1, n):
                a = dp(arr[i], arr[j])
                if a:
                    answer = max(answer, 2 + a)
        return answer

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        v = {j:i for i,j in enumerate(arr)}
        # dp = {(i,j):-1 for i in arr for j in arr}
        dp = [[-1] * n for _ in range(n)]
        def f(a:int, b:int) -> int:
            if dp[v[a]][v[b]] != -1:
                return dp[v[a]][v[b]]
            dp[v[a]][v[b]] = 0
            # if a + b in arr:
            if a + b in v:
                dp[v[a]][v[b]] = 1 + f(b, a+b)
            return dp[v[a]][v[b]]
        answer = 0
        for i in range(n):
            for j in range(i + 1, n):
                a = f(arr[i], arr[j])
                if a:
                    answer = max(answer, 2 + a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5,6,7,8]
        o = 5
        self.assertEqual(s.lenLongestFibSubseq(i), o)

    def test_two(self):
        s = Solution()
        i = [1,3,7,11,12,14,18]
        o = 3
        self.assertEqual(s.lenLongestFibSubseq(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)