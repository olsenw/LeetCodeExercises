# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s and an integer k. It is possible to choose one of the first
    k letters of s and append it at the end of the string.

    Return the lexicographically smallest string possible after applying the
    above step any number of times.
    '''
    # needed leetcode solution
    # https://leetcode.com/problems/orderly-queue/solution/
    # tricky because there are only two cases that matter
    # k == 1 allows the string to rotate and smallest is the answer
    # k >= 2 allows any possible permutation to occur (including sorted string)
    # coming to this 2nd realization is the crux of the problem
    def orderlyQueue(self, s: str, k: int) -> str:
        # only rotations are possible the smallest is the answer
        if k == 1:
            best = s
            for _ in range(len(s)):
                s = s[1:] + s[0]
                if s < best:
                    best = s
            return best
        # if k is greater than two any possible permutation is possible
        return "".join(sorted(s))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "cba"
        j = 1
        o = "acb"
        self.assertEqual(s.orderlyQueue(i,j), o)

    def test_two(self):
        s = Solution()
        i = "baaca"
        j = 3
        o = "aaabc"
        self.assertEqual(s.orderlyQueue(i,j), o)

    def test_three(self):
        s = Solution()
        i = "acaaa"
        j = 1
        o = "aaaac"
        self.assertEqual(s.orderlyQueue(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)