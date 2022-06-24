# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq

class Solution:
    '''
    Given an array target of n integers. From a starting array arr
    consisting of n 1's the following procedure may be performed:
    * let x be the sum of all elements currently in the array.
    * choose index i such that 0 <= i < n and set the value of arr at
      index i to x.
    * this procedure may be repeated as many times as needed.

    Return true if it is possible to construct the target array from
    arr, otherwise, return false.
    '''
    # help from discussion post by anuvabtest
    # https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/2189520/Python-easy-solution-324-ms-simple-beginer-friendly-solution
    # needed help to figure out big chunk removal (ie modulus use)
    def isPossible(self, target: List[int]) -> bool:
        s = sum(target)
        h = [-t for t in target]
        heapq.heapify(h)
        while h[0] < -1:
            n = -h[0]
            s -= n
            if s == 1:
                return True
            if s >= n or s == 0 or n % s == 0:
                return False
            n %= s
            s += n
            heapq.heapreplace(h, -n)
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [9,3,5]
        o = True
        self.assertEqual(s.isPossible(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,2]
        o = False
        self.assertEqual(s.isPossible(i), o)

    def test_three(self):
        s = Solution()
        i = [8,5]
        o = True
        self.assertEqual(s.isPossible(i), o)

    def test_four(self):
        s = Solution()
        i = [9,9,9]
        o = False
        self.assertEqual(s.isPossible(i), o)

    def test_five(self):
        s = Solution()
        i = [1,1000000000]
        o = True
        self.assertEqual(s.isPossible(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)