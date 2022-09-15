# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter

class Solution:
    '''
    An integer array original is transformed into a doubled array
    changed by appending twice the value of every element in original,
    and then randomly shuffling the resulting array.

    Given an array changed, return original if changed is a doubled
    array. If changed is not a doubled array, return an empty array.
    The elements in original may be returned in any order.
    '''
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        a = []
        c = Counter()
        for n in sorted(changed, reverse=True):
            if 2 * n in c and c[2 * n]:
                c[2 * n] -= 1
                a.append(n)
            else:
                c[n] += 1
        return a if c.total() == 0 else []

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,4,2,6,8]
        o = [1,3,4]
        self.assertEqual(sorted(s.findOriginalArray(i)), o)

    def test_two(self):
        s = Solution()
        i = [6,3,0,1]
        o = []
        self.assertEqual(s.findOriginalArray(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = []
        self.assertEqual(s.findOriginalArray(i), o)

    def test_four(self):
        s = Solution()
        i = [1]
        o = []
        self.assertEqual(s.findOriginalArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)