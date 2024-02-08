# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array arr of length n where arr[i] = (2 * i) + 1 for all valid
    values of i (ie, 0 <= i < n).

    In one operation select two indices x and y where 0 <= x, y < n and subtract
    1 from arr[x] and add 1 to arr[y] (ie perform arr[x] -= 1 and arr[y] += 1).
    The goal is to make all the elements of the array equal. It is guaranteed
    that all the elements of the array can be made equal using some operations.

    Given an integer n, the length of the array, return the minimum number of
    operations needed to make all the elements of arr equal.
    '''
    def minOperations(self, n: int) -> int:
        l = [2 * i + 1 for i in range(n)]
        t = sum(l) // n
        a = sum(t - i for i in l[:n//2+n%2])
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        o = 2
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = 6
        o = 9
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)