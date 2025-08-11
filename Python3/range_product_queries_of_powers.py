# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n, there exists a 0-indexed array called powers,
    composed of the minimum number of powers of 2 that sum to n. The array is
    sorted in non-decreasing order, and there is only one way to form the array.

    Also given a 0-indexed 2D integer array queries, where
    queries[i] = [lefti, righti]. Each queries[i] represents a query for the
    product of all powers[j] with lefti <= j <= righti.

    Return an array answers, equal in length to queries, where answers[i] is the
    answer to the ith query. Since the answer to the ith query may be too large,
    each answers[i] should be returned modulo 10^9 + 7.
    '''
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        m = 10**9 + 7
        powers = []
        for i in range(32):
            j = 1 << i
            if n & j:
                powers.append(j)
        answer = []
        for i,j in queries:
            k = 0
            while k < i:
                k += 1
            a = powers[k]
            k += 1
            while k <= j: #len(powers) and powers[k] <= j:
                a = ((a % m) * (powers[k] % m)) % m
                k += 1
            answer.append(a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 15
        j = [[0,1],[2,2],[0,3]]
        o = [2,4,64]
        self.assertEqual(s.productQueries(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [[0,0]]
        o = [2]
        self.assertEqual(s.productQueries(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [[0,0]]
        o = [2]
        self.assertEqual(s.productQueries(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)