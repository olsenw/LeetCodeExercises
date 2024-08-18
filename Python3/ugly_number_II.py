# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An ugly number is a positive integer whose prime factors are limited to 2,
    3, and 5.

    Given an integer n, return the nth ugly number.
    '''
    # based on hints
    # wrong (skips numbers that are have 2,3,5 combo like 10 or 12)
    def nthUglyNumber_wrong(self, n: int) -> int:
        twos = 1
        threes = 1
        fives = 1
        ugly = 0
        for _ in range(n):
            ugly = min(twos, threes, fives)
            while twos <= ugly:
                twos *= 2
            while threes <= ugly:
                threes *= 3
            while fives <= ugly:
                fives *= 5
        return ugly

    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        ugly = 0
        for _ in range(n):
            while h[0] <= ugly:
                heapq.heappop(h)
            ugly = heapq.heappop(h)
            heapq.heappush(h, ugly * 2)
            heapq.heappush(h, ugly * 3)
            heapq.heappush(h, ugly * 5)
        return ugly

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10
        o = 12
        self.assertEqual(s.nthUglyNumber(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.nthUglyNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)