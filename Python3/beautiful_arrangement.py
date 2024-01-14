# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import itertools
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Suppose there are n integers labeled 1 through n. A permutation of those n
    integers perm (1-indexed) is considered a beautiful arrangement if for every
    i (1 <= i <= n), either of the following is true:
    * perm[i] is divisible by i.
    * i is divisible by perm[i]

    Given an integer n, return the number of the beautiful arrangements that can
    be constructed.
    '''
    # O(n * n!) not feasible
    def countArrangement_brute(self, n: int) -> int:
        def valid(test):
            for i,j in enumerate(test, 1):
                if not (j % i == 0 or i % j == 0):
                    return False
            return True
        return sum(valid(t) for t in itertools.permutations(list(range(1,n+1))))

    # backtracking based on the LeetCode editorial
    # O(k) where k is the number valid permutations
    def countArrangement(self, n: int) -> int:
        v = [False] * (n + 1)
        answer = 0
        def calculate(n, p, v):
            nonlocal answer
            if p > n:
                answer += 1
            for i in range(1, n+1):
                if not v[i-1] and (p % i == 0 or i % p == 0):
                    v[i-1] = True
                    calculate(n, p+1, v)
                    v[i-1] = False
        calculate(n, 1, v)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        o = 2
        self.assertEqual(s.countArrangement(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.countArrangement(i), o)

    def test_three(self):
        s = Solution()
        i = 5
        o = 10
        self.assertEqual(s.countArrangement(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)