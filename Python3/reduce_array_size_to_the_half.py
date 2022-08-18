# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter

class Solution:
    '''
    Given an integer array arr, a set of integers can be chosen and all
    occurrences of those integers will be removed from the array.

    Return the minimum size of the set so that at least half of the
    integers of the array are removed.
    '''
    def minSetSize(self, arr: List[int]) -> int:
        l = len(arr)
        v = sorted(Counter(arr).values(), reverse=True)
        i = 0
        while l > len(arr) // 2:
            l -= v[i]
            i += 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,3,3,3,5,5,5,2,2,7]
        o = 2
        self.assertEqual(s.minSetSize(i), o)

    def test_two(self):
        s = Solution()
        i = [7,7,7,7,7,7]
        o = 1
        self.assertEqual(s.minSetSize(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)